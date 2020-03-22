import inspect
import time
import grpc
from locust import (TaskSet,task,events,Locust)
from gevent._semaphore import Semaphore
import importlib
from locust.clients import LocustResponse, ResponseContextManager
from locust.exception import LocustError

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()

# events.hatch_complete += on_hatch_complete


class GrpcSession(object):

    suffix = '_grpc'
    default_package = 'locust_package.protos_gen'

    def __init__(self, host, **kwargs):
        super(GrpcSession, self).__init__()
        self.host = host
        self.grpc_port = kwargs['grpc_port']
        self.compile_file = kwargs['compile_files']

        # Check for basic authentication
        # parsed_url = urlparse(self.base_url)
        # if parsed_url.username and parsed_url.password:
        #     netloc = parsed_url.hostname
        #     if parsed_url.port:
        #         netloc += ":%d" % parsed_url.port
        #
        #     # remove username and password from the base_url
        #     self.base_url = urlunparse((parsed_url.scheme, netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
        #     # configure requests to use basic auth
        #     self.auth = HTTPBasicAuth(parsed_url.username, parsed_url.password)

    def _build_conn(self):
        return grpc.insecure_channel('{}:{}'.format(self.host, self.grpc_port))

    def dynamic_import(self):
        stub = importlib.import_module(
            ''.join([str(file) for file in self.compile_file
                     if str(file).endswith(self.suffix)]),
            package=self.default_package)

        descriptor = importlib.import_module(
            ''.join([str(file) for file in self.compile_file
                     if not str(file).endswith(self.suffix)]),
            package=self.default_package)
        if stub is None or descriptor is None:
            raise Exception('Failed to generate grpc code!')
        return stub, descriptor

    def request(self, method, catch_response=False, **kwargs):

        grpc_conn = self._build_conn()
        stub_compile, descriptor = self.dynamic_import()
        try:
            class_names = inspect.getmembers(stub_compile, inspect.isclass)
            stub_class = ''.join([items[0] for items in class_names if items[0].endswith('Stub')])
            stub = getattr(stub_compile, stub_class)(channel=grpc_conn)
        except Exception as e:
            raise e

        # store meta data that is used when reporting the request to locust's statistics
        request_meta = {"method": method, "start_time": time.time()}

        # set up pre_request hook for attaching meta data to the request object
        args = getattr(descriptor, 'HelloRequest')(**kwargs)
        response = self._send_request_safe_mode(stub, method, args)
        request_meta["response_time"] = (time.time() - request_meta["start_time"]) * 1000
        print(response)
        if catch_response:
            response.locust_request_meta = request_meta
            return ResponseContextManager(response)
        try:
            if response.errCode != 0:
                raise Exception
            events.request_success.fire(
                request_type='grpc',
                name=method,
                response_time=request_meta["response_time"],
                response_length=0
            )
        except Exception as e:
            events.request_failure.fire(
                request_type='grpc',
                name=method,
                response_time=request_meta["response_time"],
                response_length=0,
                exception=e
            )

        return response

    @staticmethod
    def _send_request_safe_mode(stub, method, args):
        """
        Send an HTTP request, and catch any exception that might occur due to connection problems.

        Safe mode has been removed from requests 1.x.
        """

        try:
            return getattr(stub, method)(args)
        except Exception as e:
            r = LocustResponse()
            r.error = e
            r.status_code = 0  # with this status_code, content returns None
            return r


class GrpcLocust(Locust):
    def __init__(self):
        super(GrpcLocust, self).__init__()
        if self.host is None:
            raise LocustError("You must specify the base host. "
                              "Either in the host attribute in the Locust class, "
                              "or on the command line using the --host option.")
        session = GrpcSession(
            self.host, grpc_port=self.grpc_port,
            compile_files=self.compile_files)
        self.client = session

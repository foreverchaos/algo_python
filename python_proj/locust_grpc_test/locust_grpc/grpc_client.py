import inspect
import time
from pathlib import Path

import grpc
import grpc_tools.protoc as protoc
from locust import events, Locust
from gevent._semaphore import Semaphore
import importlib
from locust.clients import LocustResponse, ResponseContextManager
from locust.exception import LocustError
import os

# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()


# def on_hatch_complete(**kwargs):
#     all_locusts_spawned.release()

# events.hatch_complete += on_hatch_complete


COMPILE_PACKAGE = 'protos.gen'


class GrpcSession(object):

    def __init__(self, host, **kwargs):
        super(GrpcSession, self).__init__()
        self.host = host
        self.grpc_stub = kwargs['grpc_stub']
        self.descriptor_module = kwargs['descriptor_module']
        self.service_name = kwargs['service_name']
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

    def request(self, method, catch_response=False, **kwargs):
        # store meta data that is used when reporting the request to locust's statistics
        request_methods = self.descriptor_module.DESCRIPTOR.services_by_name[
            self.service_name.replace('Stub', '')].methods
        input_class_name = [m.input_type.name for m in request_methods if m.name == method]

        if len(input_class_name) != 1:
            raise Exception('Duplicated definition of methods!')

        args = getattr(self.descriptor_module, input_class_name[0])(**kwargs)
        request_meta = {"method": method, "start_time": time.time()}

        # set up pre_request hook for attaching meta data to the request object
        response = self._send_request_safe_mode(self.grpc_stub, method, args)
        request_meta["response_time"] = (time.time() - request_meta["start_time"]) * 1000
        request_meta["content_size"] = (0 if not hasattr(response, 'message')
                                        else len(getattr(response, 'message')))

        if catch_response:
            response.locust_request_meta = request_meta
            return ResponseContextManager(response)
        try:
            if not hasattr(response, 'message'):
                raise Exception
            events.request_success.fire(
                request_type='grpc',
                name=method,
                response_time=request_meta["response_time"],
                response_length=request_meta["content_size"]
            )
        except Exception as e:
            events.request_failure.fire(
                request_type='grpc',
                name=method,
                response_time=request_meta["response_time"],
                response_length=request_meta["content_size"],
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

    proto_path = '{}{}protos'.format(os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), os.sep)

    print('proto path is' + proto_path)

    def __init__(self):
        super(GrpcLocust, self).__init__()
        if self.host is None:
            raise LocustError("You must specify the base host. "
                              "Either in the host attribute in the Locust class, "
                              "or on the command line using the --host option.")

        self.grpc_channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.grpc_port))

        self.stub_module, self.descriptor_module = self._dynamic_import()
        self.service_name, self.grpc_stub = self._build_grpc_stub()

        session = GrpcSession(self.host, grpc_stub=self.grpc_stub,
                              descriptor_module=self.descriptor_module,
                              service_name=self.service_name)
        self.client = session

    def _dynamic_import(self):
        stub = importlib.import_module(
            '.{}'.format(self.grpc_gen_stub), package=COMPILE_PACKAGE)

        descriptor = importlib.import_module(
            '.{}'.format(self.grpc_gen_des), package=COMPILE_PACKAGE)

        if stub is None or descriptor is None:
            raise Exception('Failed to generate grpc code!')
        return stub, descriptor

    def _build_grpc_stub(self):
        try:
            class_names = inspect.getmembers(self.stub_module, inspect.isclass)
            service_name = ''.join([items[0] for items in class_names
                                    if items[0].endswith('Stub')])
            if hasattr(self.stub_module, service_name):
                return service_name, getattr(self.stub_module, service_name)(channel=self.grpc_channel)
        except Exception as e:
            raise e

    @classmethod
    def import_service(cls, service=None):
        cls.grpc_gen_stub = '{}_pb2_grpc'.format(service)
        cls.grpc_gen_des = '{}_pb2'.format(service)
        cls.service = service

    def run(self, runner=None):
        with self.grpc_channel:
            super(GrpcLocust, self).run(runner=None)

    def setup(self):
        protoc.main((
            '',
            '--proto_path={proto_path}'.format(
                proto_path=self.proto_path),
            '--python_out={proto_path}{sep}gen'.format(
                proto_path=self.proto_path, sep=os.sep),
            '--grpc_python_out={proto_path}{sep}gen'.format(
                proto_path=self.proto_path, sep=os.sep),
            '{proto_path}{sep}{service}.proto'.format(
                proto_path=self.proto_path, sep=os.sep, service=self.service)
        ))

    def teardown(self):
        for file in Path('{}{}gen'.format(self.proto_path, os.sep)).iterdir():
            if file.name.startswith(self.service):
                file.unlink()




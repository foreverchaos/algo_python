import inspect
from locust import TaskSet, task, between
from locust_grpc.grpc_client import GrpcLocust
from locust_influxdb.data_to_influx import expose_metrics

expose_metrics(influx_host='172.17.0.1', influx_port=8086, interval_ms=2000)


class UserBehaviour(TaskSet):

    @task(1)
    def test_say_hello(self):
        self.client.request('SayHello', name='louis')

    @task(2)
    def test_say_hello_again(self):
        self.client.request('SayHelloAgain', city='shanghai')


def grpc_service(name=None, service=None):
    if inspect.isclass(name):
        test_class = name
        test_class.import_service()
        return test_class
    else:
        def wrapper(cls):
            cls.import_service(service)
            return cls
    return wrapper


@grpc_service(service='helloworld')
class WebsiteUser(GrpcLocust):
    # host = "172.17.0.1"
    grpc_port = 50051
    task_set = UserBehaviour
    wait_time = between(1, 2)


if __name__ == '__main__':
    u = WebsiteUser()
    u.run()
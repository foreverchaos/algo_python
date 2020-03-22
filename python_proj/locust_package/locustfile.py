from locust import HttpLocust, TaskSet, task, between
from .locust_grpc.grpc_client import GrpcLocust
from locust_package.locust_influx import expose_metrics
from grpc_tools import protoc
import os
# expose_metrics(influx_host='localhost', influx_port='8086', interval_ms=2000)


class BaseBehaviour(TaskSet):

    def setup(self):
        protoc.main((
            '',
            '--proto_path=./protos',
            '--python_out=./protos_gen',
            '--grpc_python_out=./protos_gen',
            'helloworld.proto'
        ))

    def teardown(self):
        for file in os.listdir('./protos_gen'):
            if not file.startswith('__init__'):
                os.remove(file)


class UserBehaviour(BaseBehaviour):

    @task(1)
    def say_hello(self):
        self.client.request('SayHello', name='czl')
    # @task(1)
    # def news_international(self):
    #     self.client.get("/about/")


class WebsiteUser(GrpcLocust):
    host = "localhost"
    grpc_port = 50051
    compile_files = ['helloworld_pb2', 'helloworld_pb2_grpc']
    task_set = UserBehaviour
    wait_time = between(1, 2)


if __name__ == '__main__':
    u = WebsiteUser()
    u.run()
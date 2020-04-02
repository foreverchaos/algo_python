import grpc
import rpc.helloworld_pb2 as helloworld_pb2
import rpc.helloworld_pb2_grpc as helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='czl'))
        print("Greeter client received: " + response.message)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='daydaygo'))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
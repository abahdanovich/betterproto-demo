import asyncio
import grpc

from .helloworld_pb2 import HelloReply, HelloRequest
from .helloworld_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class Greeter(GreeterServicer):
    async def SayHello(self, request: HelloRequest, context):
        return HelloReply(message=f"Hello, {request.name}!")


async def serve():
    server = grpc.aio.server()
    add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())

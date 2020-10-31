import asyncio
from dataclasses import dataclass
from typing import List

import grpc
from faker import Faker

from .helloworld import (
    FooBar,
    HelloNestedReply,
    HelloReply,
    HelloRequest,
    SomeCollection,
    SomeRecord,
    SomeRequest,
)
from .helloworld_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


def generate_fake_collection(rows_num: int) -> List[SomeRecord]:
    fake = Faker()
    return [
        SomeRecord(
            name=fake.name(),
            address=fake.address(),
            age=fake.random_int(0, 100),
            country=fake.country_code(),
        )
        for _ in range(rows_num)
    ]


@dataclass
class FakeData:
    some_collection: List[SomeRecord]


fake_data = FakeData(some_collection=[])


class Greeter(GreeterServicer):
    async def SayHello(self, request: HelloRequest, context):
        return HelloReply(message=[f"Hello, {request.name}!"])

    async def SayHelloStream(self, request: HelloRequest, context):
        yield HelloReply(message=[f"Hello, {request.name}!"])

    async def SayHelloNested(self, request: HelloRequest, context):
        return HelloNestedReply(message=[FooBar(foo="Hello", bar=request.name)])

    async def GetSomeCollection(self, request: SomeRequest, context):
        return SomeCollection(rows=fake_data.some_collection[: request.rows_num])

    async def GetSomeStream(self, request: SomeRequest, context):
        for row in fake_data.some_collection[: request.rows_num]:
            yield row


async def serve():
    print("Starting server")
    server = grpc.aio.server()
    add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    await server.start()
    await server.wait_for_termination()


def run():
    print("Preparing data")
    fake_data.some_collection = generate_fake_collection(10_000)
    asyncio.run(serve())


if __name__ == "__main__":
    run()

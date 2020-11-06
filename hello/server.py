import asyncio
import datetime
import sys
from dataclasses import dataclass
from typing import List

from faker import Faker  # type: ignore
from grpclib.server import Server, Stream
from grpclib.utils import graceful_exit

from .helloworld import (CustomProps, FooBar, HelloNestedReply, HelloReply,
                         HelloRequest, HelloStreamReply, SomeCollection,
                         SomeRecord, SomeRequest)
from .helloworld_grpc import GreeterBase


def generate_fake_collection(rows_num: int) -> List[SomeRecord]:
    fake = Faker()
    return [
        SomeRecord(
            name=fake.name(),
            address=fake.address(),
            age=fake.random_int(0, 100),
            country=fake.country_code(),
            custom_props=CustomProps(
                foo=fake.random_int(0, 100),
                ts=fake.date_time(tzinfo=datetime.timezone.utc),
                is_active=fake.boolean(),
            ),
        )
        for _ in range(rows_num)
    ]


@dataclass
class FakeData:
    some_collection: List[SomeRecord]


fake_data = FakeData(some_collection=[])


class Greeter(GreeterBase):
    async def SayHello(self, stream: Stream[HelloRequest, HelloReply]):
        request = await stream.recv_message()
        if request:
            await stream.send_message(HelloReply(message=[f"Hello, {request.name}!"]))

    async def SayHelloStream(self, stream: Stream[HelloRequest, HelloStreamReply]):
        request = await stream.recv_message()
        if request:
            await stream.send_message(
                HelloStreamReply(message=f"Hello, {request.name}!")
            )

    async def SayHelloNested(self, stream: Stream[HelloRequest, HelloNestedReply]):
        request = await stream.recv_message()
        if request:
            await stream.send_message(
                HelloNestedReply(message=[FooBar(foo="Hello", bar=request.name)])
            )

    async def GetSomeCollection(self, stream: Stream[SomeRequest, SomeCollection]):
        request = await stream.recv_message()
        if request:
            await stream.send_message(
                SomeCollection(rows=fake_data.some_collection[: request.rows_num])
            )

    async def GetSomeStream(self, stream: Stream[SomeRequest, SomeRecord]):
        request = await stream.recv_message()
        if request:
            for row in fake_data.some_collection[: request.rows_num]:
                await stream.send_message(row)


async def main(host="127.0.0.1", port=50051):
    server = Server([Greeter()])
    with graceful_exit([server]):
        await server.start(host, port)
        print(f"Serving on {host}:{port}")
        await server.wait_closed()


def run(rows_count: str = "20_000"):
    print(f"Preparing data ({rows_count} rows)")
    fake_data.some_collection = generate_fake_collection(int(rows_count))
    asyncio.run(main())


if __name__ == "__main__":
    run(*sys.argv[1:])

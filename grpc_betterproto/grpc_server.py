import asyncio
import sys
from dataclasses import dataclass
from typing import List

from grpclib.server import Server, Stream
from grpclib.utils import graceful_exit

from data_gen import generate_fake_domain_records, DomainRecord
from .helloworld import (FooBar, HelloNestedReply, HelloReply,
                         HelloRequest, HelloStreamReply, SomeCollection,
                         SomeRecord, SomeRequest, CustomProps)
from .helloworld_grpc import GreeterBase


@dataclass
class FakeData:
    rows: List[DomainRecord]

    def __init__(self) -> None:
        self.rows = []


fake_data = FakeData()


class Greeter(GreeterBase):
    async def say_hello(self, stream: Stream[HelloRequest, HelloReply]) -> None:
        request = await stream.recv_message()
        if request:
            await stream.send_message(HelloReply(message=[f"Hello, {request.name}!"]))

    async def say_hello_stream(self, stream: Stream[HelloRequest, HelloStreamReply]) -> None:
        request = await stream.recv_message()
        if request:
            await stream.send_message(
                HelloStreamReply(message=f"Hello, {request.name}!")
            )

    async def say_hello_nested(self, stream: Stream[HelloRequest, HelloNestedReply]) -> None:
        request = await stream.recv_message()
        if request:
            await stream.send_message(
                HelloNestedReply(message=[FooBar(foo="Hello", bar=request.name)])
            )

    async def get_some_collection(self, stream: Stream[SomeRequest, SomeCollection]) -> None:
        request = await stream.recv_message()
        if request:
            rows = [
                _from_domain_record(row)
                for row in fake_data.rows[: request.rows_num]
            ]
            await stream.send_message(
                SomeCollection(rows=rows)
            )

    async def get_some_stream(self, stream: Stream[SomeRequest, SomeRecord]) -> None:
        request = await stream.recv_message()
        if request:
            for row in fake_data.rows[: request.rows_num]:
                await stream.send_message(_from_domain_record(row))


def _from_domain_record(r: DomainRecord) -> SomeRecord:
    rcp = r.custom_props

    return SomeRecord(
        name=r.name,
        address=r.address,
        age=r.age,
        country=r.country,
        custom_props=CustomProps(
            foo=rcp.foo,
            ts=rcp.ts,
            is_active=rcp.is_active
        )
    )


async def main(host: str = "127.0.0.1", port: int = 50051) -> None:
    server = Server([Greeter()])
    with graceful_exit([server]):
        await server.start(host, port)
        print(f"Serving on {host}:{port}")
        await server.wait_closed()


def run() -> None:
    rows_num: str = sys.argv[1] if len(sys.argv) > 1 else '20_000'
    print(f"Preparing data ({rows_num} rows)")
    fake_data.rows = generate_fake_domain_records(int(rows_num))
    asyncio.run(main())


if __name__ == "__main__":
    run()

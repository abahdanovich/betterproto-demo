import asyncio
from contextlib import contextmanager

from grpclib.client import Channel

from .helloworld import GreeterStub, SomeRecord


@contextmanager
def ManagedChannel(*args, **kwargs):
    channel = Channel(*args, **kwargs)
    try:
        yield channel
    finally:
        channel.close()


async def main():
    with ManagedChannel(host="127.0.0.1", port=50051) as channel:
        stub = GreeterStub(channel)

        # response = await stub.say_hello(name="world")
        # print(response.message)

        # async for response in stub.say_hello_stream(name="world"):
        #     print(response.message)

        # response = await stub.say_hello_nested(name="world")
        # print(response.message)

        # response = await stub.get_some_collection(rows_num=10_000)
        # for row in response.rows:
        #     print(row.to_json())

        rows = [row async for row in stub.get_some_stream(rows_num=20_000)]
        print(len(rows))


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()

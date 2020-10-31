import asyncio
from contextlib import contextmanager
from grpclib.client import Channel
from .helloworld_pb2 import GreeterStub


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
        response = await stub.say_hello(name="world")
    print("Greeter client received: " + response.message)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()

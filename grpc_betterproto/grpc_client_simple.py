import asyncio

import sys
from grpclib.client import Channel

from .helloworld import GreeterStub


async def main(rows_num: int) -> None:
    async with Channel(host="127.0.0.1", port=50051) as channel:
        stub = GreeterStub(channel)

        response = await stub.get_some_collection(rows_num=rows_num)
        print(len(response.rows))
        print(response.rows[0].to_json())


def run() -> None:
    rows_num: str = sys.argv[1] if len(sys.argv) > 1 else '20_000'
    asyncio.run(main(int(rows_num)))


if __name__ == "__main__":
    run()

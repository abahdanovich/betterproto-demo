import asyncio

import sys
from grpclib.client import Channel
from tqdm.asyncio import tqdm

from .helloworld import GreeterStub, SomeRecord


async def main(rows_num: int) -> None:
    async with Channel(host="127.0.0.1", port=50051) as channel:
        stub = GreeterStub(channel)

        row: SomeRecord
        async for row in tqdm(stub.get_some_stream(rows_num=rows_num), total=rows_num):
            pass

        print(row.to_json())


def run() -> None:
    rows_num: str = sys.argv[1] if len(sys.argv) > 1 else '20_000'
    asyncio.run(main(int(rows_num)))


if __name__ == "__main__":
    run()

import asyncio
# import json
import sys
# import timeit
# from time import perf_counter
# from typing import List
from tqdm.asyncio import tqdm
# import orjson
from grpclib.client import Channel

from .helloworld import GreeterStub, SomeRecord


async def main(rows_num: int) -> None:
    async with Channel(host="127.0.0.1", port=50051) as channel:
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

        # p1 = perf_counter()
        # rows: List[SomeRecord] = [row async for row in stub.get_some_stream(rows_num=rows_num)]
        # p2 = perf_counter()

        # print(f"Fetching {len(rows)} rows from server took: {round(p2-p1, 3)} s")

        # t1 = timeit.timeit('out = map(lambda row:   json.dumps(row.to_dict()), rows)', number=20, globals={'rows': []})
        # print(' json:', round(t1 * 1000, 3), 'ms')

        # t2 = timeit.timeit('out = map(lambda row: orjson.dumps(row).decode(),  rows)', number=20, globals={'rows': []})
        # print('orjson:', round(t2 * 1000, 3), 'ms')

        # for row in rows:
        #     print(json.dumps(row.to_dict()))

        # for row in rows:
        #     print(orjson.dumps(row).decode())

        # row: SomeRecord
        # async for row in stub.get_some_stream(rows_num=rows_num):
        #     print(orjson.dumps(row).decode())

        _: SomeRecord
        async for _ in tqdm(stub.get_some_stream(rows_num=rows_num), total=rows_num):
            pass


def run() -> None:
    rows_num: str = sys.argv[1] if len(sys.argv) > 1 else '20_000'
    asyncio.run(main(int(rows_num)))


if __name__ == "__main__":
    run()

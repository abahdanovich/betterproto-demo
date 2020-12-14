# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: helloworld.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncGenerator, List, Optional

import betterproto
import grpclib


@dataclass
class HelloRequest(betterproto.Message):
    name: str = betterproto.string_field(1)


@dataclass
class HelloReply(betterproto.Message):
    message: List[str] = betterproto.string_field(1)


@dataclass
class HelloStreamReply(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass
class FooBar(betterproto.Message):
    foo: str = betterproto.string_field(1)
    bar: str = betterproto.string_field(2)


@dataclass
class HelloNestedReply(betterproto.Message):
    message: List["FooBar"] = betterproto.message_field(1)


@dataclass
class SomeRequest(betterproto.Message):
    rows_num: int = betterproto.uint32_field(1)


@dataclass
class CustomProps(betterproto.Message):
    foo: Optional[int] = betterproto.message_field(1, wraps=betterproto.TYPE_INT32)
    ts: datetime = betterproto.message_field(2)
    is_active: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )


@dataclass
class SomeRecord(betterproto.Message):
    name: str = betterproto.string_field(1)
    address: str = betterproto.string_field(2)
    age: int = betterproto.uint32_field(3)
    country: str = betterproto.string_field(4)
    custom_props: "CustomProps" = betterproto.message_field(5)


@dataclass
class SomeCollection(betterproto.Message):
    rows: List["SomeRecord"] = betterproto.message_field(1)


class GreeterStub(betterproto.ServiceStub):
    async def say_hello(self, *, name: str = "") -> HelloReply:
        request = HelloRequest()
        request.name = name

        return await self._unary_unary(
            "/helloworld.Greeter/say_hello",
            request,
            HelloReply,
        )

    async def say_hello_stream(
        self, *, name: str = ""
    ) -> AsyncGenerator[HelloStreamReply, None]:
        request = HelloRequest()
        request.name = name

        async for response in self._unary_stream(
            "/helloworld.Greeter/say_hello_stream",
            request,
            HelloStreamReply,
        ):
            yield response

    async def say_hello_nested(self, *, name: str = "") -> HelloNestedReply:
        request = HelloRequest()
        request.name = name

        return await self._unary_unary(
            "/helloworld.Greeter/say_hello_nested",
            request,
            HelloNestedReply,
        )

    async def get_some_collection(self, *, rows_num: int = 0) -> SomeCollection:
        request = SomeRequest()
        request.rows_num = rows_num

        return await self._unary_unary(
            "/helloworld.Greeter/get_some_collection",
            request,
            SomeCollection,
        )

    async def get_some_stream(
        self, *, rows_num: int = 0
    ) -> AsyncGenerator[SomeRecord, None]:
        request = SomeRequest()
        request.rows_num = rows_num

        async for response in self._unary_stream(
            "/helloworld.Greeter/get_some_stream",
            request,
            SomeRecord,
        ):
            yield response
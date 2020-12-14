import datetime
from dataclasses import dataclass
from typing import List, Any

import strawberry

from data_gen import generate_fake_domain_records, DomainRecord


@dataclass
class FakeData:
    rows: List[DomainRecord]

    def __init__(self) -> None:
        self.rows = []


@strawberry.type
class CustomProps:
    foo: int
    ts: datetime.datetime
    is_active: bool


@strawberry.type
class SomeRecord:
    name: str
    address: str
    age: int
    country: str
    custom_props: CustomProps


@strawberry.type
class Query:
    @strawberry.field
    def some_collection(self, info: Any, rows_num: int) -> List[SomeRecord]:
        return [
            _from_domain_record(row)
            for row in fake_data.rows[: rows_num]
        ]


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


fake_data = FakeData()
fake_data.rows = generate_fake_domain_records(20_000)

schema = strawberry.Schema(query=Query)

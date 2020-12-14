import datetime
from dataclasses import dataclass
from typing import List

from faker import Faker


@dataclass()
class CustomProps:
    foo: int
    ts: datetime.datetime
    is_active: bool


@dataclass()
class DomainRecord:
    name: str
    address: str
    age: int
    country: str
    custom_props: CustomProps


def generate_fake_domain_records(rows_num: int) -> List[DomainRecord]:
    fake = Faker()
    return [
        DomainRecord(
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

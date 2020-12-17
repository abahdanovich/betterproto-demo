from dataclasses import dataclass
from typing import List, Any

from ariadne import QueryType, gql, make_executable_schema, convert_kwargs_to_snake_case
from ariadne.asgi import GraphQL

from data_gen import generate_fake_domain_records, DomainRecord


@dataclass
class FakeData:
    rows: List[DomainRecord]

    def __init__(self) -> None:
        self.rows = []


type_defs = gql("""
    type CustomProps {
        foo: Int!
        ts: String!
        isActive: Boolean!
    }
    type SomeRecord {
        name: String!
        address: String!
        age: Int!
        country: String!
        customProps: CustomProps!
    }
    type Query {
        someCollection(rowsNum: Int!): [SomeRecord!]
    }
""")

query = QueryType()


@query.field("someCollection")
@convert_kwargs_to_snake_case
def some_collection(_: Any, info: Any, rows_num: int) -> List[dict]:
    return [
        _from_domain_record(row)
        for row in fake_data.rows[: rows_num]
    ]


def _from_domain_record(r: DomainRecord) -> dict:
    rcp = r.custom_props

    return dict(
        name=r.name,
        address=r.address,
        age=r.age,
        country=r.country,
        customProps=dict(
            foo=rcp.foo,
            ts=rcp.ts.isoformat(),
            isActive=rcp.is_active
        )
    )


fake_data = FakeData()
fake_data.rows = generate_fake_domain_records(20_000)

schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)



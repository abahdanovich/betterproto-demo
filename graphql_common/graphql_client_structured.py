import datetime
import json
from typing import List

from gqlclient import GraphQLClient
from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder


@dataclass
class Parameters:
    rowsNum: int


@dataclass
class CustomProps:
    foo: int
    ts: datetime.datetime
    isActive: bool


@dataclass
class SomeRecord:
    name: str
    address: str
    age: int
    country: str
    customProps: CustomProps


def main() -> None:
    client = GraphQLClient(gql_uri="http://localhost:8000/graphql")
    parameters = Parameters(rowsNum=20_000)
    response: List[SomeRecord] = client.execute_gql_query(query_base="someCollection", query_response_cls=SomeRecord, query_parameters=parameters)
    assert response
    print(len(response))
    print(json.dumps(response[0], default=pydantic_encoder))


if __name__ == "__main__":
    main()

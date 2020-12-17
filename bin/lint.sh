#!/usr/bin/env bash

set -e

cd "`dirname $0`"
cd ..

poetry run pylint grpc_betterproto/ graphql_*/ data_gen/ || true
poetry run mypy grpc_betterproto/ graphql_*/ data_gen/

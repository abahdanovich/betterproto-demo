#!/usr/bin/env bash

set -e

cd "`dirname $0`"
cd ..

poetry run pylint grpc_bench/ || true
poetry run mypy grpc_bench/

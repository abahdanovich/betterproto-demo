#!/usr/bin/env bash

set -e

cd "`dirname $0`"
cd ..

poetry run grpc-server

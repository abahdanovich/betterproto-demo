#!/usr/bin/env bash

cd `dirname $0`
DIR=`basename $PWD`
cd ..

poetry run python -m grpc_tools.protoc \
    -I $DIR \
    --python_betterproto_out=$DIR \
    --grpc_python_out=$DIR \
    helloworld.proto 

sed -i 's/import helloworld_pb2 as helloworld__pb2/from . import helloworld as helloworld__pb2/g' $DIR/helloworld_pb2_grpc.py
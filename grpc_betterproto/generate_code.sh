#!/usr/bin/env bash

cd `dirname $0`
DIR=`basename $PWD`
cd ..

poetry run python -m grpc_tools.protoc \
    -I $DIR \
    --python_betterproto_out=$DIR \
    --grpclib_python_out=$DIR \
    helloworld.proto 

sed -i 's/import helloworld_pb2/from . import helloworld/g' $DIR/helloworld_grpc.py
sed -i 's/helloworld_pb2/helloworld/g' $DIR/helloworld_grpc.py
gRPC (betterproto)
==================

Server
------

```
python -m grpc_betterproto.grpc_server
```

Client (simple)
------

```
time python -m grpc_betterproto.grpc_client_simple | jq
```

Output:

```
real	0m4,145s
```

Client (streaming)
------

```
time python -m grpc_betterproto.grpc_client_streaming | jq
```

Output:

```
real	0m2,783s
```

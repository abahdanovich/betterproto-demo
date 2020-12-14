gRPC (betterproto)
==================

Server
------

```
poetry run grpc-betterproto-server
```

Output:

```
Preparing data (20_000 rows)
Serving on 127.0.0.1:50051
```

Client
------

```
poetry run grpc-betterproto-client
```

Output:

```
100% | 20000/20000 [00:02<00:00, 7062.40it/s]
```

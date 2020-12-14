Server
======

```
poetry run grpc-server
```

Output:

```
Preparing data (20_000 rows)
Serving on 127.0.0.1:50051
```

Client
======

```
poetry run grpc-client
```

Output:

```
100% | 20000/20000 [00:02<00:00, 7062.40it/s]
```
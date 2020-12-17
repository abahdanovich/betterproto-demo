GraphQL (strawberry)
====================

Server
------

```
strawberry server -h 127.0.0.1 graphql_strawberry.graphql_server
```


Client (raw)
------

```
time python -m graphql_strawberry.graphql_client_raw | jq
```

Output:

```
real	0m1,435s
```

Client (structured)
------

```
time python -m graphql_strawberry.graphql_client_structured | jq
```

Output:

```
real	0m3,484s
```

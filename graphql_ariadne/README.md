GraphQL (ariadne)
====================

Server
------

```
uvicorn graphql_ariadne.graphql_server:app
```


Client (raw)
------

```
time python -m graphql_common.graphql_client_raw | jq
```

Output:

```
real	0m1,315s
```

Client (structured)
------

```
time python -m graphql_common.graphql_client_structured | jq
```

Output:

```
real	0m3,400s
```

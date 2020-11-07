Server
======

```
python -m hello.server 100000
```

Output:

```
Preparing data (100000 rows)
Serving on 127.0.0.1:50051
```

Client
======

```
python -m hello.client 100000 | pv -l -s 100000 > /dev/null
```

Output:

```
# 100k 0:00:14 [6,85k/s] [=================================>] 100%
```
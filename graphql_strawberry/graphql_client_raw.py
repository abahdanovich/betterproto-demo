import json

import requests

query = '''
{
  someCollection(rowsNum: 20000) {
    name
    address
    age
    country
    customProps {
      foo
      ts
      isActive
    }
  }
}
'''


def main() -> None:
    url = 'http://localhost:8000/graphql'
    res = requests.post(url, json={
        'query': query,
    })
    res.raise_for_status()
    body = res.json()

    if 'errors' in body:
        print(res.text)
        return

    assert 'data' in body
    data = body['data']

    assert 'someCollection' in data
    coll = data['someCollection']

    assert coll
    print(len(coll))
    print(json.dumps(coll[0]))


if __name__ == "__main__":
    main()

import requests as rq
import pprint

payload = {'key1': 'value1', 'key2': 'value2'}
r = rq.get('https://httpbin.org/get', params=payload)

print(r.request)
pprint.pprint(r.request)

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Lokesh Singh"
  } ,
  { "id" : "002",
    "x" : "7",
    "name" : "Shubham Sir"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
import json
from urllib.request import urlopen


#
#VVisit and check  https://randomuser.me/
#


with urlopen("https://randomuser.me/api/?results=20") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

li =[]

from collections import namedtuple
Person = namedtuple('Person', ['name' ,'email'])

for item in data['results']:
    name = item['name']['first'] + " " + item['name']['last']
    email = item['email']
    li.append(Person(name , email))


print("li length ->" , len(li))
for i in li:
    print(i)
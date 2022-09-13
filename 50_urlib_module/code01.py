import json
from urllib.request import urlopen
url = 'https://randomuser.me/api/0.8'
file = urlopen(url)
li = list(file)
#for line in file:
#    print(line)

print('########################################################')
for l in li :
    print(l)
print('########################################################')
data =""
for l in li:
    decode_data = l.decode("utf-8")
    #decode_data = decode_data.replace("\n", '')
    data += decode_data
print(data)

jsondata = json.loads(data)
print(type(jsondata)) #Expecting dict
print('########################################################')
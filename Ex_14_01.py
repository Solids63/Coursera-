import urllib.request, urllib.parse, urllib.error
import json


address = 'http://py4e-data.dr-chuck.net/comments_1457353.json'
url = urllib.request.urlopen(address).read()
info = json.loads(url)

result = 0

for count in info['comments']:
    result = result + count['count']
print(result)



import os
import tempfile
import argparse
import json

lst = {}
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="dictionary key")
parser.add_argument("-v", "--val", help="value of dictionary item")
args = parser.parse_args()

key = args.key
val = args.val

if key and val:
    lst[key] = [val]

elif key and val is None:
    print('value')
else:
    print('wrong input')


print(lst)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'a') as json_file:
#    for _ in [lst]:
     json.dump(lst, json_file)
#     json_file.write(lst)

#  b = json.loads(open(json_file))
#  print(b)
with open(storage_path, 'r') as json_file:
#    json_file.seek(0)
#    line = json_file.read()
    data = json.load(json_file)
    print(type(data))
    print(data)




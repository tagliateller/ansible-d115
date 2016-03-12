import json
import sys
#from pprint import pprint

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

#print sys.argv[1]
#print sys.argv[2]

result = "0"

for item in data:
  if item["title"] == sys.argv[2]:
    result = str(item["id"])

#result = 66

#sys.stdout = result
exit (result)


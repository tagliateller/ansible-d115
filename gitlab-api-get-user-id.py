import json
import sys

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

result = "0"

for item in data:
  if item["username"] == sys.argv[2]:
    result = str(item["id"])

#result = 66

#sys.stdout = result
exit (result)


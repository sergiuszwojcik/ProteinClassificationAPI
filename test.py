import urllib.request
import json

with urllib.request.urlopen('http://scop2.mrc-lmb.cam.ac.uk/graph/restapi/chart?term=SF:3000098') as response:
   html = json.loads(response.read())

# print(html)

for line in html:
    print(line)
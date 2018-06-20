import json

f = open('./json/CoC.json')
j = json.load(f)
counties = {}

print j['2010']['CoC Name']

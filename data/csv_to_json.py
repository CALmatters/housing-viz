import json
import codecs
import os
import pandas as pd

state_dict = {}
CoC_dict = {}

for f in os.listdir('./csv'):
    df = pd.read_csv('./csv/'+f)
    if 'state' in f and 'Change' not in f:
        row = df.loc[df['State'] == 'CA']
        di = row.to_dict()
        sub_dict = {}
        for k,v in di.items():
            for nested_v in v.items():
                sub_dict[k] = nested_v[1]
        year = f[5:9]
        state_dict[year] = sub_dict
    elif 'Change' in f:
        row = df.loc[df['state'] == 'CA']
        row.to_json('./json/stateChange.json')
    elif 'Mergers' not in f: # all CoC csv's
        df = df.fillna("None")
        # print df.isnull().sum()
        rows = [df[df['CoC Number'].str.contains('CA')]]
        for r in rows:
            di = r.to_dict()
            sub_dict = {}
            for k,v in di.items():
                for nested_v in v.items():
                    sub_dict[k] = nested_v[1]
            year = f[3:7]
            CoC_dict[year] = sub_dict


state_json = json.dumps(state_dict)
CoC_json = json.dumps(CoC_dict)

state_f = open('./json/state.json','w')
state_f.write(state_json)
state_f.close()

CoC_f = open('./json/CoC.json','w')
CoC_f.write(CoC_json)
CoC_f.close()

totals = {}
# Get national totals for each year
for f in os.listdir('./csv'):
    df = pd.read_csv('./csv/'+f)
    if 'state' in f and 'Change' not in f:
        year = f[5:9]
        col = 'Total Homeless, ' + year
        totals[year] = (pd.to_numeric(df[col], errors='coerce')).sum()

print totals

# {'2016': 1099856.0, '2010': 1274154.0, '2007': 1294516.0, '2015': 1129416.0, '2014': 1152900.0, '2008': 1279568.0, '2009': 1260454.0, '2011': 1247576.0, '2017': 1107484.0, '2013': 1180728.0, '2012': 1243106.0}

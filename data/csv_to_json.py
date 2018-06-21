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
        rows = df[df['CoC Number'].str.contains('CA')]
        year = f[3:7]
        rows = rows.drop('CoC Number',axis=1)
        col_list = ['CoC Name', 'Sheltered Homeless, '+year, 'Unsheltered Homeless, '+year]
        rows = rows[col_list]
        rows = rows.rename(index=str,columns={'CoC Name': 'County'})
        CoC_dict[year] = rows

dfs = []
for v in CoC_dict.values():
    dfs.append(v)

df_final = reduce(lambda left,right: pd.merge(left,right,on='County'), dfs)
df_final['the_geom'] = 'Polygon'
df_final.to_csv('./csv/maps.csv')

state_json = json.dumps(state_dict)
# CoC_json = json.dumps(CoC_dict)

state_f = open('./json/state.json','w')
state_f.write(state_json)
state_f.close()

# CoC_f = open('./json/CoC.json','w')
# CoC_f.write(CoC_json)
# CoC_f.close()

totals = {}
# Get national totals for each year
for f in os.listdir('./csv'):
    df = pd.read_csv('./csv/'+f)
    if 'state' in f and 'Change' not in f:
        year = f[5:9]
        col = 'Total Homeless, ' + year
        totals[year] = df.loc[df['State'] == 'Total'][col]

# print totals

# {2007: 647258.0, 2008: 639784.0, 2009: 630227.0, 2010: 637077.0, 2011: 623788.0, 2012: 621553.0, 2013: 590364.0, 2014: 576450.0, 2015: 564708.0, 2016: 549928.0, 2017: 553742.0}

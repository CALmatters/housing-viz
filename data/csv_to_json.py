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
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Santa Clara.*$)', 'Santa Clara')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Francisco.*$)', 'San Francisco')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Alameda.*$)', 'Alameda')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Sacramento.*$)', 'Sacramento')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Sonoma.*$)', 'Sonoma')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Contra Costa.*$)', 'Contra Costa')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Benito.*$)', 'San Benito')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Marin.*$)', 'Marin')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Santa Cruz.*$)', 'Santa Cruz')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Stanislaus.*$)', 'Stanislaus')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Joaquin.*$)', 'San Joaquin')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Mateo.*$)', 'San Mateo')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Tulare.*$)', 'Tulare')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Santa Clara.*$)', 'Santa Clara')

        madera = rows.loc[rows['CoC Name'] == 'Fresno/Madera County CoC']
        madera['CoC Name'] = madera['CoC Name'].str.replace(r'(^.*Madera.*$)', 'Madera')
        rows.append(madera,ignore_index=True)

        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Fresno.*$)', 'Fresno') # Fresno and Madera were combined

        nevada = rows.loc[rows['CoC Name'] == 'Roseville/Rocklin/Placer, Nevada Counties CoC']
        nevada['CoC Name'] = nevada['CoC Name'].str.replace(r'(^.*Nevada.*$)', 'Nevada')
        rows.append(nevada,ignore_index=True)
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Placer.*$)', 'Placer') # Nevada and Placer were combined

        siskiyou = rows.loc[rows['CoC Name'] == 'Redding/Shasta, Siskiyou, Lassen, Plumas, Del Norte, Modoc, Sierra Counties CoC']
        siskiyou['CoC Name'] = siskiyou['CoC Name'].str.replace(r'(^.*Siskiyou.*$)', 'Siskiyou')
        rows.append(siskiyou,ignore_index=True)

        plumas = rows.loc[rows['CoC Name'] == 'Redding/Shasta, Siskiyou, Lassen, Plumas, Del Norte, Modoc, Sierra Counties CoC']
        plumas['CoC Name'] = plumas['CoC Name'].str.replace(r'(^.*Plumas.*$)', 'Plumas')
        rows.append(plumas,ignore_index=True)

        delNorte = rows.loc[rows['CoC Name'] == 'Redding/Shasta, Siskiyou, Lassen, Plumas, Del Norte, Modoc, Sierra Counties CoC']
        delNorte['CoC Name'] = delNorte['CoC Name'].str.replace(r'(^.*Del Norte.*$)', 'Del Norte')
        rows.append(delNorte,ignore_index=True)

        sierra = rows.loc[rows['CoC Name'] == 'Redding/Shasta, Siskiyou, Lassen, Plumas, Del Norte, Modoc, Sierra Counties CoC']
        sierra['CoC Name'] = sierra['CoC Name'].str.replace(r'(^.*Sierra.*$)', 'Sierra')
        rows.append(sierra,ignore_index=True)

        lassen = rows.loc[rows['CoC Name'] == 'Redding/Shasta, Siskiyou, Lassen, Plumas, Del Norte, Modoc, Sierra Counties CoC']
        lassen['CoC Name'] = lassen['CoC Name'].str.replace(r'(^.*Lassen.*$)', 'Lassen')
        rows.append(lassen,ignore_index=True)

        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Shasta.*$)', 'Shasta') # Shasta, Siskiyou, Plumas, Del Norte, Modoc, Sierra, and Lassen were combined - might need to duplicate the row
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Napa.*$)', 'Napa')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Solano.*$)', 'Solano')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Butte.*$)', 'Butte')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Merced.*$)', 'Merced')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Yolo.*$)', 'Yolo')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Humboldt.*$)', 'Humboldt')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Trinity.*$)', 'Trinity')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Sutter.*$)', 'Sutter')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*El Dorado.*$)', 'El Dorado')

        calaveras = rows.loc[rows['CoC Name'] == 'Amador, Calaveras, Tuolumne and Mariposa Counties CoC']
        calaveras['CoC Name'] = calaveras['CoC Name'].str.replace(r'(^.*Calaveras.*$)', 'Calaveras')
        rows.append(calaveras,ignore_index=True)

        tuolumne = rows.loc[rows['CoC Name'] == 'Amador, Calaveras, Tuolumne and Mariposa Counties CoC']
        tuolumne['CoC Name'] = tuolumne['CoC Name'].str.replace(r'(^.*Tuolumne.*$)', 'Tuolumne')
        rows.append(tuolumne,ignore_index=True)

        mariposa = rows.loc[rows['CoC Name'] == 'Amador, Calaveras, Tuolumne and Mariposa Counties CoC']
        mariposa['CoC Name'] = mariposa['CoC Name'].str.replace(r'(^.*Mariposa.*$)', 'Mariposa')
        rows.append(mariposa,ignore_index=True)

        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Amador.*$)', 'Amador') #Amador, Calaveras, Tuolumne, and Mariposa were consolidated
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Del Norte.*$)', 'Del Norte')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Los Angeles.*$)', 'Los Angeles')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Diego.*$)', 'San Diego')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Orange.*$)', 'Orange')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Santa Barbara.*$)', 'Santa barbara')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Kern.*$)', 'Kern')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Long Beach.*$)', 'Long Beach')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Pasadena.*$)', 'Pasadena')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Riverside.*$)', 'Riverside')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Bernardino.*$)', 'San Bernardino')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Ventura.*$)', 'Ventura')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Glendale.*$)', 'Glendale') # Add up all of the LA County rows
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Imperial.*$)', 'Imperial')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*San Luis Obispo.*$)', 'San Luis Obispo')
        rows['CoC Name'] = rows['CoC Name'].str.replace(r'(^.*Mendocino.*$)', 'Mendocino')

        year = f[3:7]

        rows = rows.drop('CoC Number',axis=1)
        col_list = ['CoC Name', 'Sheltered Homeless, '+year, 'Unsheltered Homeless, '+year]
        rows = rows[col_list]
        # TODO: Consolidate all entries that fall under LA
        rows = rows.rename(index=str,columns={'CoC Name': 'County'})
        CoC_dict[year] = rows

dfs = []
for v in CoC_dict.values():
    dfs.append(v)

df_final = reduce(lambda left,right: pd.merge(left,right,on='County'), dfs)
df_final.to_csv('./homelessness3.csv')

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

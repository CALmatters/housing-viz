import pandas as pd

df = pd.read_csv('./homelessness_edited.csv')
df.drop('cartodb_id',axis=1)

s = 'Total Homeless, '
year = 2007
while year < 2018:
    same_year = []
    for col in df.columns:
        if str(year) in col:
            same_year.append(df[col])
        if len(same_year) == 2:
            title = s+str(year)
            df[title] = same_year[0] + same_year[1]
            break
    year+=1

df.to_csv('./homelessness_totals.csv')

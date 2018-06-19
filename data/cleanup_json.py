import json

# Clean up state.json
f = open('./json/state.json')
j = json.load(f)
d = {}
families = {}
veterans = {}
unsheltered = {}
for year in j:
    s = 'Total Homeless, '
    s_families = 'Homeless People in Families, '
    s_veterans = 'Homeless Veterans, '
    s_unsheltered = 'Unsheltered Homeless, '
    d[year] = j[year][s + year]
    families[year] = j[year][s_families + year]
    veterans[year] = j[year][s_veterans + year]
    unsheltered[year] = j[year][s_unsheltered + year]

# Total counts
state_counts = json.dumps(d)
state_counts_f = open('./json/state_counts.json','w')
state_counts_f.write(state_counts)
state_counts_f.close()

# Counts for families
families_counts = json.dumps(families)
families_counts_f = open('./json/family_counts.json','w')
families_counts_f.write(families_counts)
families_counts_f.close()

# Counts for veterans
veteran_counts = json.dumps(veterans)
veteran_counts_f = open('./json/veteran_counts.json','w')
veteran_counts_f.write(veteran_counts)
veteran_counts_f.close()

# Counts for unsheltered
unsheltered_counts = json.dumps(unsheltered)
u_f = open('./json/unsheltered_counts.json','w')
u_f.write(unsheltered_counts)
u_f.close()

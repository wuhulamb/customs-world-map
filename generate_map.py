import json, csv

# Read CSV
csv_lookup = {}
with open('country-iso.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        csv_lookup[row['ISO_A3']] = row

# Read TopoJSON
with open('world.topo.json') as f:
    topo = json.load(f)

# Enrich geometries with trade data
geoms = topo['objects']['World_Bank_Official_Boundaries_Admin_0']['geometries']
for g in geoms:
    iso3 = g['properties']['ISO_A3']
    row = csv_lookup.get(iso3)
    g['properties']['trade_partner_name'] = row['贸易伙伴名称'] if row else ''
    g['properties']['trade_partner_code'] = row['贸易伙伴编码'] if row else ''

# Write enriched data to external JS file (global variable)
with open('world_data.js', 'w', encoding='utf-8') as f:
    f.write('var worldTopo = ')
    json.dump(topo, f, ensure_ascii=False, separators=(',', ':'))
    f.write(';\n')

print('Done: world_data.js generated')

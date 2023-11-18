"""

Takes data from https://mtgjson.com/


"""

import json

path = '../LCI.json'

with open(path, 'r', encoding='utf-8') as fo:
    data = json.load(fo)

result = dict()
print(f'Parsing {data["data"]["name"]}')
for card in data['data']['cards']:
    if 'mtgArenaId' not in card['identifiers']:
        continue
    arena_id = card['identifiers']['mtgArenaId']
    name = card['name']
    print(f'Found [{arena_id}]: {name}')
    result[arena_id] = name


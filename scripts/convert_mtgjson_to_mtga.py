"""

Takes data from https://mtgjson.com/ and writes it to mtga.json

# mtgajson format

id: {name: str, coloridentity: [str]}


"""

import json

path = '../data/LCI.json'

with open(path, 'r', encoding='utf-8') as fo:
    data = json.load(fo)

result = dict()
print(f'Parsing {data["data"]["name"]}')
for card in data['data']['cards']:
    if 'mtgArenaId' not in card['identifiers']:
        continue
    arena_id = card['identifiers']['mtgArenaId']
    name = card['name']
    coloridentity = card['colorIdentity']
    print(f'Found [{arena_id}]: {name}')
    result[arena_id] = {'name': name, 'coloridentity': coloridentity}

with open('../data/mtga.json', 'w+') as fo:
    json.dump(result, fo)


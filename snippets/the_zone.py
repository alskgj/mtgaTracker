# import requests
#
# url = 'https://mtgazone.com/the-lost-caverns-of-ixalan-lci-limited-tier-list/'
#
# response = requests.get(url)
# print(response)
#
# with open('../data/mtgazone_all_sample.html', 'w', encoding='utf-8') as fo:
#     fo.write(response.text)
import json

from bs4 import BeautifulSoup

with open ('../data/mtgazone_all_sample.html', 'r', encoding='utf-8') as fo:
    data = fo.read()

soup = BeautifulSoup(data, 'html.parser')

result = {}
for row in soup.tbody.find_all('tr'):
    fields = row.find_all('td')
    # there are 8 fields, containing name, rarity, rating in each row
    for i in range(8):
        name = fields[0+i*3].text
        rating = fields[2+i*3].text
        if name:
            result[name]=float(rating)
print(result)

with open('../data/mtgazone.json', 'w') as fo:
    json.dump(result, fo)

import json

CardID = int
CardName = str

with open('data/mtga.json', 'r') as fo:
    card_data = json.load(fo)

with open('data/mtgazone.json', 'r') as fo:
    card_ratings = json.load(fo)

def get_name(card: CardID):
    return card_data[str(card)]

def get_rating(card: CardName):

    # canonize dual faced card names
    if '//' in card:
        card = card.split('//')[0].strip()

    return card_ratings[card]
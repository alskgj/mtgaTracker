import mtga
import cardinfo
from termcolor import colored

CardID = int

def printer(card_ids: [CardID]):
    cards = [cardinfo.get_card(card_id) for card_id in card_ids]
    cards.sort(key=lambda card: card.ranking, reverse=True)
    print(", ".join([f"{colored(c.name, 'red')}: {c.ranking}" for c in cards]))

mtga.subscribe_to_draft_events(printer)

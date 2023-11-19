from dataclasses import dataclass
import persistence

@dataclass
class Card:
    id: int
    name: str
    ranking: float

def get_card(card_id: int) -> Card:
    name = persistence.get_name(card_id)
    try:
        rating = persistence.get_rating(name)
    except KeyError:
        rating = 0

    return Card(card_id, name, rating)

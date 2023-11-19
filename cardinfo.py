from dataclasses import dataclass
import persistence
import enum

class Color(enum.Enum):
    W = 'White'
    U = 'Blue'
    B = 'Black'
    R = 'Red'
    G = 'Green'
    Colorless = 'Colorless'
    Multicolored = 'Multicolored'


@dataclass
class Card:
    id: int
    name: str
    ranking: float
    color: Color

def normalize_color(color_identity: [str]) -> Color:
    if len(color_identity) > 1:
        return Color.Multicolored
    elif len(color_identity) == 0:
        return Color.Colorless
    return {
        'W': Color.W,
        'U': Color.U,
        'B': Color.B,
        'R': Color.R,
        'G': Color.G,
    }[color_identity[0]]

def get_card(card_id: int) -> Card:
    name = persistence.get_name(card_id)
    color = persistence.get_color(card_id)

    try:
        rating = persistence.get_rating(name)
    except KeyError:
        rating = 0

    return Card(card_id, name, rating, normalize_color(color))

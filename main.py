import mtga
import cardinfo
from termcolor import colored
import os
from cardinfo import Color

CardID = int

color_map = {
        Color.W: 'white',
        Color.U: 'blue',
        Color.B: 'magenta',
        Color.R: 'red',
        Color.G: 'green',
        Color.Colorless: 'light_grey',
        Color.Multicolored: 'yellow',
}

def printer(event: mtga.DraftEvent):
    cards = [cardinfo.get_card(card_id) for card_id in event.card_ids]
    cards.sort(key=lambda card: card.ranking, reverse=True)

    pack_number, pick_number = event.pack_number, event.pick_number

    os.system('cls')
    print(f'{colored(f"Pack {pack_number}, pick {pick_number}", attrs=["bold"])}')
    print(f'Best card: {colored(f"{cards[0].name}: {cards[0].ranking}", color_map[cards[0].color])}')

    for color in color_map:
        print(f'{color.value:<20}', end='')
        print(colored(", ".join([f'{c.name}: {c.ranking}' for c in cards if c.color == color]), color_map[color]))



mtga.subscribe_to_draft_events(printer)







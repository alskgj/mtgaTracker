"""
Interacts with the game mtga itself (through the Player log file)

"""
import dataclasses
import json
from collections.abc import Callable, Sequence
from typing import Any
import threading
import time
import os

LOG_PATH = os.path.join(os.getenv('APPDATA'), '..', r'LocalLow\Wizards Of The Coast\MTGA\Player.log')

@dataclasses.dataclass
class DraftEvent:
    card_ids: [int]
    pack_number: int
    pick_number: int

def subscribe_to_draft_events(func: Callable[[DraftEvent], Any], log_path = LOG_PATH):
    threading.Thread(target=feed_draft_events, args=(func, log_path)).start()


def feed_draft_events(func: Callable[[DraftEvent], Any], log_path) -> [int]:
    fo = open(log_path, 'r')

    while True:
        line = fo.readline()
        if line:
            if 'CardsInPack' in line.strip():
                func(extract_cards_from_logline(line))
        else:
            time.sleep(0.1)

def extract_cards_from_logline(line) -> DraftEvent:
    data = line.split('LogBusinessEvents ')[1]
    payload = json.loads(json.loads(json.loads(data)['request'])['Payload'])
    return DraftEvent(payload['CardsInPack'], payload['PackNumber'], payload['PickNumber'])


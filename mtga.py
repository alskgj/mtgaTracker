"""
Interacts with the game mtga itself (through the Player log file)

"""

import json
from collections.abc import Callable, Sequence
from typing import Any
import threading
import time

LOG_PATH = r'C:\Users\nen\AppData\LocalLow\Wizards Of The Coast\MTGA\Player.log'

def subscribe_to_draft_events(func: Callable[[Sequence[int]], Any], log_path = LOG_PATH):

    threading.Thread(target=feed_draft_events, args=(func, log_path)).start()


def feed_draft_events(func: Callable[[Sequence[int]], Any], log_path) -> [int]:
    fo = open(log_path, 'r')

    while True:
        line = fo.readline()
        if line:
            if 'CardsInPack' in line.strip():
                func(extract_cards_from_logline(line))
        else:
            time.sleep(0.1)

def extract_cards_from_logline(line) -> [int]:
    data = line.split('LogBusinessEvents ')[1]
    return json.loads(json.loads(json.loads(data)['request'])['Payload'])['CardsInPack']


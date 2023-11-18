"""
Example data

[UnityCrossThreadLogger]==> LogBusinessEvents {"id":"2c9fe89b-1007-47cf-ac43-23faf1532573","request":"{\"Type\":1912,\"TransId\":\"2c9fe89b-1007-47cf-ac43-23faf1532573\",\"Payload\":\"{\\\"PlayerId\\\":null,\\\"ClientPlatform\\\":null,\\\"DraftId\\\":\\\"8036008b-7696-4b42-adf6-1aa2aa8a13bc\\\",\\\"EventId\\\":\\\"PremierDraft_LCI_20231114\\\",\\\"SeatNumber\\\":6,\\\"PackNumber\\\":3,\\\"PickNumber\\\":12,\\\"PickGrpId\\\":87210,\\\"CardsInPack\\\":[87133,87410,87210,87364],\\\"AutoPick\\\":false,\\\"TimeRemainingOnPick\\\":5.7346015,\\\"EventType\\\":24,\\\"EventTime\\\":\\\"2023-11-18T09:37:35.0148422Z\\\"}\"}"}
"""

import os
import time

path = r'C:\Users\nen\AppData\LocalLow\Wizards Of The Coast\MTGA\Player.log'

print(os.path.exists(path))

def main():
    fo = open(path, 'r')

    while True:
        line = fo.readline()
        if line:
            if line.strip():
                print(f'found new line: [{line[:-1]}]')
        else:
            time.sleep(0.1)


if __name__ == '__main__':
    main()



import json
with open('../test_data/sample_line.txt') as fo:
    data = fo.read()

print(json.loads(json.loads(json.loads(data)['request'])['Payload']))

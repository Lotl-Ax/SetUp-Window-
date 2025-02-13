import json

with open ("output.json", "r") as cf:
    ojson = json.load(cf)

    for item in ojson['crimes']:
        if item['crimeType'] == 'Burglary':
            print(f'{item['location']}, {item['LSOACode']}, {item['LSOAName']}')

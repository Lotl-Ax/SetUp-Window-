import json

'''
month = input(str('Enter a month: ')).lower()
year = input(str('Enter a Year: '))

months = {
    'january':1,
    'february':2,
    'march':3,
    'april':4,
    'may':5,
    'june':6,
    'july':7,
    'august':8,
    'september':9,
    'october':10,
    'november':11,
    'december':12
}
monthint = months[month]
date = f'{year}-0{monthint}'
print(date)
'''

with open ("output.json", "r") as cf:
    ojson = json.load(cf)

    for item in ojson['crimes']:
        if item['crimeType'] != 'Burglary':
            if item['location'] != 'No Location':
                print(f'{item['location']}, {item['LSOACode']}, {item['LSOAName']}')

import matplotlib.pyplot as Mplt
import json

crime = ['Anti-social behaviour', 'Bicycle theft', 'Burglary', 'Criminal damage and arson', 'Drugs', 'Possession of weapons', 'Public order', 'Robbery', 'Shoplifting', 'Theft from the person', 'Vehicle crime', 'Violence and sexual offences']
amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open ("output.json", "r") as cf:   #  loading JSON file
    ojson = json.load(cf)
    
    for item in ojson['crimes']:
          
        if item['crimeType'] in crime: 
            this_crime = item['crimeType']
            index = crime.index(this_crime)
            amount[index] += 1





font = {'family':'serif','color':'darkred','size':10}

Mplt.barh(crime, amount, height=0.5, color=['blue', 'green'])

Mplt.ylabel('Crime', fontdict=font)
Mplt.xlabel('Amount', fontdict=font)

Mplt.title('Crime amounts')

Mplt.tight_layout()

Mplt.show()

print(amount)
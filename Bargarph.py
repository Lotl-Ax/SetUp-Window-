import matplotlib.pyplot as Mplt
import json

crime = ['Antisocial behaviour', 'Bicycle Theft', 'Burglary', 'Criminal Damage', 'Drugs', 'Possession of Weapons', 'Public Order', 'Robbery', 'Shoplifting', 'Theft from Person', 'Vehicle Crime', 'Violence and Sexual offences']
amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open ("output.json", "r") as cf:   #  loading JSON file
    ojson = json.load(cf)
    
    for item in ojson['crimes']:
          
        for item['crimeType'] in crime: 
            index = crime.index(item['crimeType'])
            amount[index] += 1





font = {'family':'serif','color':'darkred','size':10}

Mplt.barh(crime, amount, height=0.5, color=['blue', 'green'])

Mplt.ylabel('Crime', fontdict=font)
Mplt.xlabel('Amount', fontdict=font)

Mplt.title('Crime amounts')

Mplt.tight_layout()

Mplt.show()

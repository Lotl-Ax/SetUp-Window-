# program to get teh data for graphs that can be manually inputted into the main program, means main doesnt have to fetch the data itself

import json

crimeCount = {
        'Anti-social behaviour':0,
        'Burglary':0,
        'Bicycle theft':0,
        'Criminal damage and arson':0,
        'Drugs':0,
        'Robbery':0,
        'Theft from the person':0,
        'Violence and sexual offences':0,
        'Vehicle crime':0,
        'Shoplifting':0,
        'Other theft':0,
        'Other crime':0,
        'Public order':0,
        'Possession of weapons':0

}


with open('output.json', 'r') as cf:
          ojson = json.load(cf)
          i = 0 

          for item in ojson['crimes']: # getting data that is relevant to the crimes the user wants and that have longitudes nad latitudes
                crime = item['crimeType']
                crimeCount[crime] += 1
                i += 1
              
max = 0
for thing in crimeCount:
        print(thing, crimeCount[thing])
        
        if crimeCount[thing] > max:
                max = crimeCount[thing] 
        
print(max)
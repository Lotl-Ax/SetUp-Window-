import json

#  getting largest and smallest longitudes and latitudes
#{item['location']}

'''lat_min = '51.0'
lat_max = '51.0'
long_min = '1.0'
long_max = '1.0'

with open ("output.json", "r") as cf:
    ojson = json.load(cf)

    for item in ojson['crimes']:

        if item['latitude'] != '' and item['longitude'] != '':

            cur_lat = item['latitude']
            cur_long = item['longitude']

            if cur_lat < lat_min:
                lat_min = cur_lat

            if cur_lat > lat_max:
                lat_max = cur_lat

            if cur_long < long_min:
                long_min = cur_long

            if cur_long > long_max:
                long_max = cur_long
        

            

print(f'lowest latitude: {lat_min}')
print(f'highest latitude: {lat_max}')
print(f'lowest longitude: {long_min}')
print(f'highest longitude: {long_max}')
'''

low_lat = 50.86193
high_lat = 54.951083
low_long = -0.000358
high_long = 1.269397

lat_dif = high_lat - low_lat
long_dif = high_long - low_long

#all left regions starting long = low_long
#all right regions ending long = high_long
#all top regions starting lat = high_lat
#all bottom regions ending lat = low_lat

#div lat_dif by 3 and create each row latitude boundary
#div long_dif by 4 and create each columns longitude boundary

# assign each region their boundaries

#combine set up and this
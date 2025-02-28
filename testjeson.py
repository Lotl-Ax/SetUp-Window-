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
print(f'{lat_dif} \n{long_dif}')

#all left regions (1,2,3) starting long = low_long
#all right regions (10, 11, 12) ending long = high_long
#all top regions (1,4,7,11)starting lat = high_lat
#all bottom regions (3,6,9,12)ending lat = low_lat

#div lat_dif by 3 and create each row latitude boundary
lat_divd = lat_dif/3
print(lat_divd)
#div long_dif by 4 and create each columns longitude boundary
long_divd = long_dif/4
print(long_divd)


# assign each region their boundaries

Region_boundaries = {
    'Region_1_boundaries' : {
        'top':high_lat,
        'bottom':high_lat-lat_divd,
        'left':low_long,
        'right':low_long+long_divd
    } ,

    'Region_2_boundaries' : {
        'top':high_lat-lat_divd,
        'bottom':low_lat + lat_divd,
        'left':low_long,
        'right':low_long+long_divd
    } ,

    'Region_3_boundaries' : {
        'top':low_lat + lat_divd,
        'bottom':low_lat,
        'left':low_long,
        'right':low_long+long_divd
    },

    'Region_4_boundaries' : {
        'top':high_lat,
        'bottom':high_lat-lat_divd,
        'left':low_long+long_divd,
        'right':low_long+2(long_divd)
    } ,

    'Region_5_boundaries': {
        'top':high_lat-lat_divd,
        'bottom':low_lat + lat_divd,
        'left':low_long+long_divd,
        'right':low_long+2(long_divd)
    },

    'Region_6_boundaries' : {
        'top':low_lat + lat_divd,
        'bottom':low_lat,
        'left':low_long+long_divd,
        'right':low_long+2(long_divd)
    },

    'Region_7_boundaries' : {
        'top':high_lat,
        'bottom':high_lat-lat_divd,
        'left':high_long-2(long_divd),
        'right':high_long-long_divd
    },

    'Region_8_boundaries' : {
        'top':high_lat-lat_divd,
        'bottom':low_lat + lat_divd,
        'left':high_long-2(long_divd),
        'right':high_long-long_divd
    },

    'Region_9_boundaries' : {
        'top':low_lat + lat_divd,
        'bottom':low_lat,
        'left':high_long-2(long_divd),
        'right':high_long-long_divd
    },

    'Region_10_boundaries' : {
        'top':high_lat,
        'bottom':high_lat-lat_divd,
        'left':high_long-(long_divd),
        'right':high_long
    },

    'Region_11_boundaries' : {
        'top':high_lat-lat_divd,
        'bottom':low_lat + lat_divd,
        'left':high_long-(long_divd),
        'right':high_long
    },

    'Region_12_boundaries' : {
        'top':low_lat + lat_divd,
        'bottom':low_lat,
        'left':high_long-(long_divd),
        'right':high_long
    }
}
#combine set up and this



#adapt following for region assigning

with open ("output.json", "r") as cf:   #  loading JSON file
      ojson = json.load(cf)

      for item in ojson['crimes']:
          
          if item['latitu'] in crimelist: # only enters the next line if the crimeType of the current item matches one of the crimes in the crime list
              
              if item['location'] != 'No Location': # wont continue if there is no location for the cirime
                  
                  crimeCounter[item['crimeType']] += 1 #  increases the number associated with the crimeType of the current item by one
                  print(f'{item['crimeType']}, {item['location']}, {item['LSOACode']}, {item['LSOAName']}')


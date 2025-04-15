import json

crimes = ['Burglary']

crimesInfo = []
crimeinfo = ()

with open('output.json', 'r') as cf:
    ojson = json.load(cf)
    i = 0 

    for item in ojson['crimes']:

        if item['latitude'] != "" and item['longitude'] != "": 
              
            if item['crimeType'] in crimes:
                i += 1
                crimeinfo = (item['crimeId'], item['longitude'], item['latitude'])
                crimesInfo.append(crimeinfo)


low_lat = 50.86193
high_lat = 54.951083
low_long = -0.000358
high_long = 1.269397

lat_dif = high_lat - low_lat
long_dif = high_long - low_long
print(f'{lat_dif} \n{long_dif}')

lat_divd = lat_dif/3
print(lat_divd)

long_divd = long_dif/4
print(long_divd)

Region_boundaries = {
    'Region_1_boundaries' : {
            'top':high_lat,
            'bottom':(high_lat-lat_divd),
            'left':low_long,
            'right':(low_long+long_divd)
        } ,

        'Region_2_boundaries' : {
            'top':(high_lat-lat_divd),
            'bottom':(low_lat + lat_divd),
            'left':low_long,
            'right':(low_long+long_divd)
        } ,

        'Region_3_boundaries' : {
            'top':(low_lat + lat_divd),
            'bottom':low_lat,
            'left':low_long,
            'right':(low_long+long_divd)
        },

        'Region_4_boundaries' : {
            'top':high_lat,
            'bottom':(high_lat-lat_divd),
            'left':(low_long+long_divd),
            'right':(low_long+long_divd+long_divd)
        } ,

        'Region_5_boundaries': {
            'top':(high_lat-lat_divd),
            'bottom':(low_lat + lat_divd),
            'left':(low_long+long_divd),
            'right':(low_long+long_divd+long_divd)
        },

        'Region_6_boundaries' : {
            'top':(low_lat + lat_divd),
            'bottom':low_lat,
            'left':(low_long+long_divd),
            'right':(low_long+long_divd+long_divd)
        },

        'Region_7_boundaries' : {
            'top':high_lat,
            'bottom':(high_lat-lat_divd),
            'left':(high_long-long_divd-long_divd),
            'right':(high_long-long_divd)
        },

        'Region_8_boundaries' : {
            'top':(high_lat-lat_divd),
            'bottom':(low_lat + lat_divd),
            'left':(high_long-long_divd-long_divd),
            'right':(high_long-long_divd)
        },

        'Region_9_boundaries' : {
            'top':(low_lat + lat_divd),
            'bottom':low_lat,
            'left':(high_long-long_divd-long_divd),
            'right':(high_long-long_divd)
        },

        'Region_10_boundaries' : {
            'top':high_lat,
            'bottom':(high_lat-lat_divd),
            'left':(high_long-long_divd),
            'right':high_long
        },

        'Region_11_boundaries' : {
            'top':(high_lat-lat_divd),
            'bottom':(low_lat + lat_divd),
            'left':(high_long-long_divd),
            'right':high_long
        },

        'Region_12_boundaries' : {
            'top':(low_lat + lat_divd),
            'bottom':low_lat,
            'left':(high_long-long_divd),
            'right':high_long
        }
}

RegionStore  = {
    'Reg1' : [],
    'Reg2' : [],
    'Reg3' : [],
    'Reg4' : [],
    'Reg5' : [],
    'Reg6' : [],
    'Reg7' : [],
    'Reg8' : [],
    'Reg9' : [],
    'Reg10' : [],
    'Reg11' : [],
    'Reg12' : [],
}




print(i)

i = 0
for item in crimesInfo:
    Id = item[0]
    Long = float(item[1])
    Lat = float(item[2])

    for region in Region_boundaries:
        
        Reg_det = Region_boundaries[region]
        top = Reg_det['top']
        bottom = Reg_det['bottom']
        left = Reg_det['left']
        right = Reg_det['right']

        if Long >= left and Long <= right:
            if Lat <= top and Lat >= bottom: 
                i += 1
                index = list(Region_boundaries).index(region)
                print(region, index)
                x = (item[0], item[1], item[2])
                list(RegionStore.values())[index].append(x)


print(i)

for i in RegionStore:
    print(i, RegionStore[i], len(RegionStore[i]))
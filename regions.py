import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QGraphicsView, QLabel

import sys

class Map(QMainWindow):

  def __init__(self):
    
    super(Map, self).__init__()
    uic.loadUi("Wireframe.ui", self)

    self.Graphics = self.findChild(QLabel, 'Image')
    self.placeholder1 = self.findChild(QPushButton, 'marker_placeHolder1')
    self.placeholder2 = self.findChild(QPushButton, 'marker_placeHolder2')
    self.placeholder3 = self.findChild(QPushButton, 'marker_placeHolder3')
    self.placeholder4 = self.findChild(QPushButton, 'marker_placeHolder4')
    self.placeholder5 = self.findChild(QPushButton, 'marker_placeHolder5')
    self.placeholder6 = self.findChild(QPushButton, 'marker_placeHolder6')
    self.placeholder7 = self.findChild(QPushButton, 'marker_placeHolder7')
    self.placeholder8 = self.findChild(QPushButton, 'marker_placeHolder8')
    self.placeholder9 = self.findChild(QPushButton, 'marker_placeHolder9')
    self.placeholder10 = self.findChild(QPushButton, 'marker_placeHolder10')
    self.placeholder11 = self.findChild(QPushButton, 'marker_placeHolder11')
    self.placeholder12 = self.findChild(QPushButton, 'marker_placeHolder12')

    # Regions will be given specific longitude and latitude boundaries where i plan on adding crime items that fit within each Region
    # Lontide decrease left (<--) and increases right (-->)
    # Latitude increases up and decreases down
    # so top left (region 1/ placeholder 1) must have highest latitude option and lowest Lontitude option ( to other spcified location)
    # and bottom right must have lowest latitude and hightest longitude options

    self.placeholder1.setText('1')
    self.placeholder2.setText('2')
    self.placeholder3.setText('3')
    self.placeholder4.setText('4')
    self.placeholder5.setText('5')
    self.placeholder6.setText('6')
    self.placeholder7.setText('7')
    self.placeholder8.setText('8')
    self.placeholder9.setText('9')
    self.placeholder10.setText('10')
    self.placeholder11.setText('11')
    self.placeholder12.setText('12')

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
    #combine set up and this



    #adapt following for region assigning
    #for thing in crimes
    #get lat and long compare to each region bound
    #assign

    Region1 = []
    Region2 = []
    Region3 = []
    Region4 = []
    Region5 = []
    Region6 = []
    Region7 = []
    Region8 = []
    Region9 = []
    Region10 = []
    Region11 = []
    Region12 = []

    def check_Region1(item,latitude, longitude):
        r = Region_boundaries['Region_1_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region1.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region2(item, latitude, longitude):
        r = Region_boundaries['Region_2_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region2.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region3(item, latitude, longitude):
        r = Region_boundaries['Region_3_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region3.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region4(item, latitude, longitude):
        r = Region_boundaries['Region_4_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region4.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region5(item, latitude, longitude):
        r = Region_boundaries['Region_5_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region5.append(item['crimeId'])
            #endif
        #endif
    #

    def check_Region6(item, latitude, longitude):
        r = Region_boundaries['Region_6_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region6.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region7(item, latitude, longitude):
        r = Region_boundaries['Region_7_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region7.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region8(item, latitude, longitude):
        r = Region_boundaries['Region_8_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region8.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region9(item, latitude, longitude):
        r = Region_boundaries['Region_9_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region9.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region10(item, latitude, longitude):
        r = Region_boundaries['Region_10_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region10.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region11(item, latitude, longitude):
        r = Region_boundaries['Region_11_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region11.append(item['crimeId'])
            #endif
        #endif
    #enddef

    def check_Region12(item, latitude, longitude):
        r = Region_boundaries['Region_12_boundaries']

        if latitude <= str(r['top']) and latitude >= str(r['bottom']):

            if longitude >= str(r['left']) and longitude <= str(r['right']):
                Region12.append(item['crimeId'])
            #endif
        #endif
    #enddef


    with open ("output.json", "r") as cf:   #  loading JSON file
        ojson = json.load(cf)

        for item in ojson['crimes']:
          if item['latitude'] != "" or item['longitude'] != "" or item['crimeId'] == "":  
            lat = item['latitude']
            long = item['longitude']

            check_Region1(item, lat,long)
            check_Region2(item, lat,long)
            check_Region3(item, lat,long)
            check_Region4(item, lat,long)
            check_Region5(item, lat,long)
            check_Region6(item, lat,long)
            check_Region7(item, lat,long)
            check_Region8(item, lat,long)
            check_Region9(item, lat,long)
            check_Region10(item, lat,long)
            check_Region11(item, lat,long)
            check_Region12(item, lat,long)



    print(f'Num items in Region1:  {len(Region1)}')
    print(f'Num items in Region2:  {len(Region2)}')
    print(f'Num items in Region3:  {len(Region3)}')
    print(f'Num items in Region4:  {len(Region4)}')
    print(f'Num items in Region5:  {len(Region5)}')
    print(f'Num items in Region6:  {len(Region6)}')
    print(f'Num items in Region7:  {len(Region7)}')
    print(f'Num items in Region8:  {len(Region8)}')
    print(f'Num items in Region9:  {len(Region9)}')
    print(f'Num items in Region10:  {len(Region10)}')
    print(f'Num items in Region11:  {len(Region11)}')
    print(f'Num items in Region12:  {len(Region12)}')

    r1 = str(len(Region1))
    r2 = str(len(Region2))
    r3 = str(len(Region3))
    r4 = str(len(Region4))
    r5 = str(len(Region5))
    r6 = str(len(Region6))
    r7 = str(len(Region7))
    r8 = str(len(Region8))
    r9 = str(len(Region9))
    r10 = str(len(Region10))
    r11 = str(len(Region11))
    r12 = str(len(Region12))

    self.placeholder1.setText(r1)
    self.placeholder2.setText(r2)
    self.placeholder3.setText(r3)
    self.placeholder4.setText(r4)
    self.placeholder5.setText(r5)
    self.placeholder6.setText(r6)
    self.placeholder7.setText(r7)
    self.placeholder8.setText(r8)
    self.placeholder9.setText(r9)
    self.placeholder10.setText(r10)
    self.placeholder11.setText(r11)
    self.placeholder12.setText(r12)



app = QApplication(sys.argv)

window = Map()
window.show()
app.exec_()
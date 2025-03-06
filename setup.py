from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QLabel
import json 

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

    self.show()


class SetUP(QWidget):

  def __init__(self):
    
    super(SetUP, self).__init__()
    uic.loadUi("SetUP_widget.ui", self)

    self.setGeometry(750, 300, 760, 410)  # sets window position (750, 300) and its size w=600, h= 450
    self.setFixedSize(760, 410)  # fixes the window proportions so size cant be changed

    self.monthselect = self.findChild(QComboBox, 'Month_picker')
    self.monthChange = False
    self.YearSelect = self.findChild(QComboBox,'Year_Picker')
    self.yearchanged =False
    self.AntiSocial = self.findChild(QCheckBox, 'AntiSoc_Check')
    self.BikeTheft = self.findChild(QCheckBox, 'BikeTheft_Check')
    self.Drugs = self.findChild(QCheckBox, 'Drugs_Check')
    self.ShopLift = self.findChild(QCheckBox, 'Shoplift_Check')
    self.Robbery = self.findChild(QCheckBox, 'Robbery_Check')
    self.PublicOrder = self.findChild(QCheckBox, 'PubOrder_Check') 
    self.CrimDmgArson = self.findChild(QCheckBox, 'CrimDmgArs_Check')
    self.VehicleCrim = self.findChild(QCheckBox, 'Vehicle_Check')
    self.Vio_SexualOffs = self.findChild(QCheckBox, 'Vio_SexOff_Check')
    self.PersonTheft = self.findChild(QCheckBox, 'PersonTheft_Check')
    self.Weapons = self.findChild(QCheckBox, 'WeaponPossess_Check')
    self.Burglary = self.findChild(QCheckBox, 'Burglary_Check')
    self.SelectAll = self.findChild(QCheckBox, 'SelectAL_Check')
    self.Save_btn = self.findChild(QPushButton, 'Save_Button')
    self.Safe = False # setting changes as unsaved, here as its connected to Save_btn
    self.Cont_btn = self.findChild(QPushButton, 'Continue_Button')
    self.Canc_btn = self.findChild(QPushButton, 'Cancel_Button')

    self.crimelist = []
    self.crimeSelected = 0
    self.month = {
      0:'January',
      1:'February',
      2:'March',
      3:'April',
      4:'May',
      5:'June',
      6:'July',
      7:'August',
      8:'September',
      9:'October',
      10:'November',
      11:'December'
    }
    self.year = {
      0:2024,
      1:2023,
      2:2022,
      3:2021,
      4:2020
    }
    self.crimeCounter={
      'Anti-social behaviour':0,
      'Bicycle theft':0,
      'Burglary':0,
      'Criminal damage and arson':0,
      'Drugs':0,
      'Possession of weapons':0,
      'Public order':0,
      'Robbery':0,
      'Shoplifting':0,
      'Theft from the person':0,
      'Vehicle crime':0,
      'Violence and sexual offences':0
    }

    #setting event handlers
    self.monthselect.currentIndexChanged.connect(self.monthchange)
    self.YearSelect.currentIndexChanged.connect(self.YearChange)
    self.SelectAll.clicked.connect(self.Select_All)
    self.Robbery.stateChanged.connect(self.Robber_Select)
    self.CrimDmgArson.stateChanged.connect(self.CrimDmgArson_Select)
    self.Weapons.stateChanged.connect(self.Weapons_Select)
    self.Vio_SexualOffs.stateChanged.connect(self.VioSexOffs_Select)
    self.Burglary.stateChanged.connect(self.Burglary_Select)
    self.PublicOrder.stateChanged.connect(self.PublicOrder_Select)
    self.VehicleCrim.stateChanged.connect(self.VehicleCrim_Select)
    self.Drugs.stateChanged.connect(self.Drug_Select)
    self.PersonTheft.stateChanged.connect(self.PersonTheft_Select)
    self.ShopLift.stateChanged.connect(self.ShopLift_Select)
    self.BikeTheft.stateChanged.connect(self.Bike_Select)
    self.AntiSocial.stateChanged.connect(self.AntiSo_Select)
    self.Save_btn.clicked.connect(self.Saved)
    self.Cont_btn.clicked.connect(self.Cont)
    self.Canc_btn.clicked.connect(self.Cancel)
    


    self.show()
  #enddef


  def monthchange(self):
    self.monthChange = True
    self.m_index = self.monthselect.currentIndex()
    self.month_Chosen = self.month[self.m_index]
    print(self.month_Chosen)
  #enddef

  def YearChange(self):
    self.yearchanged = True
    self.y_index = self.YearSelect.currentIndex() 
    self.year_Chosen = self.year[self.y_index]
    print(self.year_Chosen)
  #enddef

  def NumCrimes_Selected(self, crime):
    

    if crime == True:

      self.crimeSelected += 1
      print(self.crimeSelected)

      if self.crimeSelected == 12:
        self.SelectAll.setChecked(True)

      #endif

    else:
      self.crimeSelected -= 1
      self.SelectAll.setChecked(False)
      print(self.crimeSelected)

    #endif
  #enddef

  def Select_All(self):

    state = self.SelectAll.checkState()

    if state == 2:
      self.Robbery.setChecked(True)
      self.CrimDmgArson.setChecked(True)
      self.VehicleCrim.setChecked(True)
      self.Vio_SexualOffs.setChecked(True)
      self.Burglary.setChecked(True)
      self.BikeTheft.setChecked(True)
      self.Weapons.setChecked(True)
      self.Drugs.setChecked(True)
      self.PersonTheft.setChecked(True)
      self.PublicOrder.setChecked(True)
      self.AntiSocial.setChecked(True)
      self.ShopLift.setChecked(True)

    else:
      self.Robbery.setChecked(False)
      self.CrimDmgArson.setChecked(False)
      self.VehicleCrim.setChecked(False)
      self.Vio_SexualOffs.setChecked(False)
      self.Burglary.setChecked(False)
      self.BikeTheft.setChecked(False)
      self.Weapons.setChecked(False)
      self.Drugs.setChecked(False)
      self.PersonTheft.setChecked(False)
      self.PublicOrder.setChecked(False)
      self.AntiSocial.setChecked(False)
      self.ShopLift.setChecked(False)

    #endif
  #enddef

  def Robber_Select(self):

    state = self.Robbery.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Robbery')
      print(self.crimelist)
      self.NumCrimes_Selected(True)
    
    else:

      #self.SelectAll.setChecked(False)
      self.crimelist.remove('Robbery')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #endef

  def CrimDmgArson_Select(self):

    state = self.CrimDmgArson.checkState()
    self.Safe = False

    if state == 2 :
      
      self.crimelist.append('Criminal damage and arson')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Criminal damage and arson')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def Weapons_Select(self):

    state = self.Weapons.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Possession of weapons')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      print(self.crimelist)
      self.crimelist.remove('Possession of weapons')
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def VioSexOffs_Select(self):

    state = self.Vio_SexualOffs.checkState()
    self.Safe = False

    if state == 2:
      
      self.crimelist.append('Violence and sexual offences')
      print(self.crimelist)
      self.NumCrimes_Selected(True)
    
    else:

      print(self.crimelist)
      self.NumCrimes_Selected(False)
      self.crimelist.remove('Violence and sexual offences')

    #endif
  #enddef

  def Burglary_Select(self):

    state = self.Burglary.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Burglary')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      print(self.crimelist)
      self.NumCrimes_Selected(False)
      self.crimelist.remove('Burglary')

    #endif
  #enddef

  def Bike_Select(self):
    self.Safe =False
    state = self.BikeTheft.checkState()

    if state == 2:

      self.crimelist.append('Bicycle theft')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Bicycle theft')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def PublicOrder_Select(self):
    self.Safe =False
    state = self.PublicOrder.checkState()

    if state == 2:

      self.crimelist.append('Public order')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Public order')
      self.NumCrimes_Selected(False)
      print(self.crimelist)

    #endif
  #enddef

  def Drug_Select(self):
    self.Safe =False
    state = self.Drugs.checkState()

    if state == 2:

      self.crimelist.append('Drugs')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Drugs')
      print(self.crimelist)

    #endif
  #enddef

  def PersonTheft_Select(self):
    self.Safe =False
    state = self.PersonTheft.checkState()

    if state == 2:

      self.crimelist.append('Theft from the person')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Theft from the person')
      print(self.crimelist)

    #endif
  #enddef

  def VehicleCrim_Select(self):

    self.Safe =False
    state = self.VehicleCrim.checkState()

    if state == 2:

      self.crimelist.append('Vehicle crime')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Vehicle crime')
      print(self.crimelist)

    #endif
  #enddef

  def ShopLift_Select(self):
    self.Safe =False
    state = self.ShopLift.checkState()

    if state == 2:

      self.crimelist.append('Shoplifting')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Shoplifting')
      print(self.crimelist)

    #endif
  #enddef

  def AntiSo_Select(self):
    self.Safe =False
    state = self.AntiSocial.checkState()

    if state == 2:

      self.crimelist.append('Anti-social behaviour')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Anti-social behaviour')
      print(self.crimelist)

    #endif
  #enddef

  def Saved(self):
    #add if statements for Month and Year for if they arent changed assume normal
    if self.monthChange == False:
      self.month_Chosen = self.month[0]

    if self.yearchanged == False:
      self.year_Chosen = self.year[0]

    self.Safe = True  #  sets safe as True, essentially 'Saving' changes
    print('Saved:')
    print(self.crimelist)
    print(self.month_Chosen)
    print(self.year_Chosen)
  #endef

  def Cont(self):

      #  Checking Cont Method can access same variables as Save Mathod

    if self.Safe == True:
      self.FetchData()
      self.setDate()
      self.OpenMap()
      window.close()
      
    else:

      msgbox = QMessageBox.warning(
        self,
        'HOLD ON',
        'Changes Are Not Saved! \nAre you sure you want to continue',
        QMessageBox.Yes | QMessageBox.No)

      if msgbox == QMessageBox.Yes:
        self.close()
      #endif
    #endif
  #enddef

  def Cancel(self):

    self.close()  #  closes the window
  #enddef

  def setDate(self):

    #  a dictionary that assigns each month its specific number e.g February = '-02' so that it matches the labelling in the JSON file
    self.monthint = {
      'January':'-01',
      'February':'-02',
      'March':'-03',
      'April':'-04',
      'May':'-05',
      'June':'-06',
      'July':'-07',
      'August':'-08',
      'September':'-09',
      'October':'-10',
      'November':'-11',
      'December':'-12'
    }
    self.monthintchosen = self.monthint[self.month_Chosen]
    self.date = (str(self.year_Chosen)+self.monthintchosen)   # creating a string for the date that is specific to what the user has selected
    print(self.date)
  #enddef

  def FetchData(self):

    with open ("output.json", "r") as cf:   #  loading JSON file
      ojson = json.load(cf)

      for item in ojson['crimes']:
          
          if item['crimeType'] in self.crimelist: # only enters the next line if the crimeType of the current item matches one of the crimes in the crime list
              
              if item['location'] != 'No Location': # wont continue if there is no location for the cirime
                  
                  self.crimeCounter[item['crimeType']] += 1 #  increases the number associated with the crimeType of the current item by one
                  print(f'{item['crimeType']}, {item['location']}, {item['LSOACode']}, {item['LSOAName']}')


    for item in self.crimeCounter:

      if item in self.crimelist:
        print(f'{item}:  {self.crimeCounter[item]}') # printing the count for each chosen crime so that i can check
  #enddef

  def OpenMap(self):
    map = Map()
    map.show()

app = QApplication(sys.argv)

window = SetUP()
window.show()
app.exec_()
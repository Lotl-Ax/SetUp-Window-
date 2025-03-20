from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QLabel
import json 

import sys


class Map(QMainWindow):

  def __init__(self, crimeid):
    
    super(Map, self).__init__()
    uic.loadUi("Wireframe.ui", self, crimeid)

    self.crimeid = crimeid

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
    self.editSetup = self.findChild(QPushButton, 'Edit_Setup_Button')

    self.Region1 = []
    self.Region2 = []
    self.Region3 = []
    self.Region4 = []
    self.Region5 = []
    self.Region6 = []
    self.Region7 = []
    self.Region8 = []
    self.Region9 = []
    self.Region10 = []
    self.Region11 = []
    self.Region12 = []

    
    self.editSetup.clicked.connect(self.open_setup)

    if self.crimeid != []:
      self.get_region_boundaries()
      self.assign_boundaries()
      self.display_region_vals()

    self.show()
  #enddef


    #Set of processes that use the data to assign each Crime to a Region

  def get_region_boundaries(self): 
      '''           Assigning Region Values and Boundaries       '''

      #latitude and longitude boundaries 

      self.low_lat = 50.86193
      self.high_lat = 54.951083
      self.low_long = -0.000358
      self.high_long = 1.269397

      # getting the difference between highest and lowest lat and long values
      self.lat_dif = self.high_lat - self.low_lat
      self.long_dif = self.high_long - self.low_long

      #dividing the lat difference by three as there are 3 rows
      self.lat_divd = self.lat_dif/3

      #dividing the long difference by 4 as there a 4 columns
      self.long_divd = self.long_dif/4

      #setting the region boundaries 
      self.Region_boundaries = {
        'Region_1_boundaries' : {
            'top':self.high_lat,
            'bottom':(self.high_lat-self.lat_divd),
            'left':self.low_long,
            'right':(self.low_long+self.long_divd)
        } ,

        'Region_2_boundaries' : {
            'top':(self.high_lat - self.lat_divd),
            'bottom':(self.low_lat + self.lat_divd),
            'left':self.low_long,
            'right':(self.low_long + self.long_divd)
        } ,

        'Region_3_boundaries' : {
            'top':(self.low_lat + self.lat_divd),
            'bottom':self.low_lat,
            'left':self.low_long,
            'right':(self.low_long + self.long_divd)
        },

        'Region_4_boundaries' : {
            'top':self.high_lat,
            'bottom':(self.high_lat - self.lat_divd),
            'left':(self.low_long + self.long_divd),
            'right':(self.low_long + self.long_divd + self.long_divd)
        } ,

        'Region_5_boundaries': {
            'top':(self.high_lat - self.lat_divd),
            'bottom':(self.low_lat + self.lat_divd),
            'left':(self.low_long + self.long_divd),
            'right':(self.low_long + self.long_divd + self.long_divd)
        },

        'Region_6_boundaries' : {
            'top':(self.low_lat + self.lat_divd),
            'bottom':self.low_lat,
            'left':(self.low_long + self.long_divd),
            'right':(self.low_long + self.long_divd + self.long_divd)
        },

        'Region_7_boundaries' : {
            'top':self.high_lat,
            'bottom':(self.high_lat - self.lat_divd),
            'left':(self.high_long - self.long_divd - self.long_divd),
            'right':(self.high_long - self.long_divd)
        },

        'Region_8_boundaries' : {
            'top':(self.high_lat - self.lat_divd),
            'bottom':(self.low_lat + self.lat_divd),
            'left':(self.high_long - self.long_divd - self.long_divd),
            'right':(self.high_long - self.long_divd)
        },

        'Region_9_boundaries' : {
            'top':(self.low_lat + self.lat_divd),
            'bottom':self.low_lat,
            'left':(self.high_long - self.long_divd - self.long_divd),
            'right':(self.high_long - self.long_divd)
        },

        'Region_10_boundaries' : {
            'top':self.high_lat,
            'bottom':(self.high_lat - self.lat_divd),
            'left':(self.high_long - self.long_divd),
            'right':self.high_long
        },

        'Region_11_boundaries' : {
            'top':(self.high_lat - self.lat_divd),
            'bottom':(self.low_lat + self.lat_divd),
            'left':(self.high_long - self.long_divd),
            'right':self.high_long
        },

        'Region_12_boundaries' : {
            'top':(self.low_lat + self.lat_divd),
            'bottom':self.low_lat,
            'left':(self.high_long - self.long_divd),
            'right':self.high_long
        }
    }
  #endif

  def assign_boundaries(self):
     with open ("output.json", "r") as cf:   #  loading JSON file
        ojson = json.load(cf)

        for item in ojson['crimes']:

          if item['latitude'] != "" or item['longitude'] != "": 

              for item['crimeId'] in self.crimeid:

                lat = item['latitude']
                long = item['longitude']

                self.check_region_1(item, lat,long)
  #enddef

  def display_region_vals(self):
      print(f'Num items in Region1:  {len(self.Region1)}')
      print(f'Num items in Region2:  {len(self.Region2)}')
      print(f'Num items in Region3:  {len(self.Region3)}')
      print(f'Num items in Region4:  {len(self.Region4)}')
      print(f'Num items in Region5:  {len(self.Region5)}')
      print(f'Num items in Region6:  {len(self.Region6)}')
      print(f'Num items in Region7:  {len(self.Region7)}')
      print(f'Num items in Region8:  {len(self.Region8)}')
      print(f'Num items in Region9:  {len(self.Region9)}')
      print(f'Num items in Region10:  {len(self.Region10)}')
      print(f'Num items in Region11:  {len(self.Region11)}')
      print(f'Num items in Region12:  {len(self.Region12)}')

      r1 = str(len(self.Region1))
      r2 = str(len(self.Region2))
      r3 = str(len(self.Region3))
      r4 = str(len(self.Region4))
      r5 = str(len(self.Region5))
      r6 = str(len(self.Region6))
      r7 = str(len(self.Region7))
      r8 = str(len(self.Region8))
      r9 = str(len(self.Region9))
      r10 = str(len(self.Region10))
      r11 = str(len(self.Region11))
      r12 = str(len(self.Region12))

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
  #enddef

  def check_region_1(self, item,latitude, longitude):
      r = self.Region_boundaries['Region_1_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region1.append(item['crimeId'])
          #endif
      else:
        self.check_region_2(item,latitude, longitude)
      #endif
  #enddef

  def check_region_2(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_2_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region2.append(item['crimeId'])
          #endif
      else:
        self.check_region_3(item,latitude, longitude)
      #endif
  #enddef

  def check_region_3(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_3_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region3.append(item['crimeId'])
          #endif
      else:
        self.check_region_4(item,latitude, longitude)
      #endif
  #enddef

  def check_region_4(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_4_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region4.append(item['crimeId'])
          #endif
      else:
        self.check_region_5(item,latitude, longitude)
      #endif
  #enddef

  def check_region_5(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_5_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region5.append(item['crimeId'])
          #endif
      else:
        self.check_region_6(item,latitude, longitude)
      #endif
  #enddef

  def check_region_6(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_6_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region6.append(item['crimeId'])
          #endif
      else:
        self.check_region_7(item,latitude, longitude)
      #endif
  #enddef

  def check_region_7(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_7_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region7.append(item['crimeId'])
          #endif
      else:
        self.check_region_8(item,latitude, longitude)
      #endif
  #enddef

  def check_region_8(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_8_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region8.append(item['crimeId'])
          #endif
      else:
        self.check_region_9(item,latitude, longitude)
      #endif
  #enddef

  def check_region_9(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_9_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region9.append(item['crimeId'])
          #endif
      else:
        self.check_region_10(item,latitude, longitude)
      #endif
  #enddef

  def check_region_10(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_10_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region10.append(item['crimeId'])
          #endif
      else:
        self.check_region_11(item,latitude, longitude)
      #endif
  #enddef

  def check_region_11(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_11_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region11.append(item['crimeId'])
          #endif
      else:
        self.check_region_12(item,latitude, longitude)
      #endif
#enddef

  def check_region_12(self, item, latitude, longitude):
      r = self.Region_boundaries['Region_12_boundaries']

      if latitude <= str(r['top']) and latitude >= str(r['bottom']):

          if longitude >= str(r['left']) and longitude <= str(r['right']):
              self.Region12.append(item['crimeId'])
          #endif
      #endif
#enddef

  def open_setup(self):

    window.show()
  #enddef



class SetUP(QWidget):

  def __init__(self):
    
    super(SetUP, self).__init__()
    uic.loadUi("SetUP_widget.ui", self)

    self.setWindowModality(
            QtCore.Qt.ApplicationModal)

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
    self.crimeid = []

    #setting event handlers
    self.monthselect.currentIndexChanged.connect(self.month_change)
    self.YearSelect.currentIndexChanged.connect(self.year_change)
    self.SelectAll.clicked.connect(self.select_all)
    self.Robbery.stateChanged.connect(self.robber_select)
    self.CrimDmgArson.stateChanged.connect(self.crim_dmg_arson_select)
    self.Weapons.stateChanged.connect(self.weapons_select)
    self.Vio_SexualOffs.stateChanged.connect(self.vio_sexoffs_select)
    self.Burglary.stateChanged.connect(self.burglary_select)
    self.PublicOrder.stateChanged.connect(self.public_order_select)
    self.VehicleCrim.stateChanged.connect(self.vehicle_crime_select)
    self.Drugs.stateChanged.connect(self.drug_select)
    self.PersonTheft.stateChanged.connect(self.person_theft_select)
    self.ShopLift.stateChanged.connect(self.shoplift_select)
    self.BikeTheft.stateChanged.connect(self.bike_select)
    self.AntiSocial.stateChanged.connect(self.antisocial_select)
    self.Save_btn.clicked.connect(self.saved)
    self.Cont_btn.clicked.connect(self.continu)
    self.Canc_btn.clicked.connect(self.cancel)
    


    self.show()
  #enddef


  def month_change(self):
    self.monthChange = True
    self.m_index = self.monthselect.currentIndex()
    self.month_Chosen = self.month[self.m_index]
    print(self.month_Chosen)
  #enddef

  def year_change(self):
    self.yearchanged = True
    self.y_index = self.YearSelect.currentIndex() 
    self.year_Chosen = self.year[self.y_index]
    print(self.year_Chosen)
  #enddef

  def num_of_crimes_selected(self, crime):
    

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

  def select_all(self):

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

  def robber_select(self):

    state = self.Robbery.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Robbery')
      print(self.crimelist)
      self.num_of_crimes_selected(True)
    
    else:

      #self.SelectAll.setChecked(False)
      self.crimelist.remove('Robbery')
      print(self.crimelist)
      self.num_of_crimes_selected(False)

    #endif
  #endef

  def crim_dmg_arson_select(self):

    state = self.CrimDmgArson.checkState()
    self.Safe = False

    if state == 2 :
      
      self.crimelist.append('Criminal damage and arson')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.crimelist.remove('Criminal damage and arson')
      print(self.crimelist)
      self.num_of_crimes_selected(False)

    #endif
  #enddef

  def weapons_select(self):

    state = self.Weapons.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Possession of weapons')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      print(self.crimelist)
      self.crimelist.remove('Possession of weapons')
      self.num_of_crimes_selected(False)

    #endif
  #enddef

  def vio_sexoffs_select(self):

    state = self.Vio_SexualOffs.checkState()
    self.Safe = False

    if state == 2:
      
      self.crimelist.append('Violence and sexual offences')
      print(self.crimelist)
      self.num_of_crimes_selected(True)
    
    else:

      print(self.crimelist)
      self.num_of_crimes_selected(False)
      self.crimelist.remove('Violence and sexual offences')

    #endif
  #enddef

  def burglary_select(self):

    state = self.Burglary.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Burglary')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      print(self.crimelist)
      self.num_of_crimes_selected(False)
      self.crimelist.remove('Burglary')

    #endif
  #enddef

  def bike_select(self):
    self.Safe =False
    state = self.BikeTheft.checkState()

    if state == 2:

      self.crimelist.append('Bicycle theft')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.crimelist.remove('Bicycle theft')
      print(self.crimelist)
      self.num_of_crimes_selected(False)

    #endif
  #enddef

  def public_order_select(self):
    self.Safe =False
    state = self.PublicOrder.checkState()

    if state == 2:

      self.crimelist.append('Public order')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.crimelist.remove('Public order')
      self.num_of_crimes_selected(False)
      print(self.crimelist)

    #endif
  #enddef

  def drug_select(self):
    self.Safe =False
    state = self.Drugs.checkState()

    if state == 2:

      self.crimelist.append('Drugs')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.num_of_crimes_selected(False)
      self.crimelist.remove('Drugs')
      print(self.crimelist)

    #endif
  #enddef

  def person_theft_select(self):
    self.Safe =False
    state = self.PersonTheft.checkState()

    if state == 2:

      self.crimelist.append('Theft from the person')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.num_of_crimes_selected(False)
      self.crimelist.remove('Theft from the person')
      print(self.crimelist)

    #endif
  #enddef

  def vehicle_crime_select(self):

    self.Safe =False
    state = self.VehicleCrim.checkState()

    if state == 2:

      self.crimelist.append('Vehicle crime')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.num_of_crimes_selected(False)
      self.crimelist.remove('Vehicle crime')
      print(self.crimelist)

    #endif
  #enddef

  def shoplift_select(self):
    self.Safe =False
    state = self.ShopLift.checkState()

    if state == 2:

      self.crimelist.append('Shoplifting')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.num_of_crimes_selected(False)
      self.crimelist.remove('Shoplifting')
      print(self.crimelist)

    #endif
  #enddef

  def antisocial_select(self):
    self.Safe =False
    state = self.AntiSocial.checkState()

    if state == 2:

      self.crimelist.append('Anti-social behaviour')
      print(self.crimelist)
      self.num_of_crimes_selected(True)

    else:

      self.num_of_crimes_selected(False)
      self.crimelist.remove('Anti-social behaviour')
      print(self.crimelist)

    #endif
  #enddef

  def saved(self):
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

  def continu(self):

      #  Checking Cont Method can access same variables as Save Mathod

    if self.Safe == True:
      self.fetch_data()
      self.set_date()
      self.hide()
      Map(self.crimeid).update()
      
      
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

  def cancel(self):

    self.close()  #  closes the window
  #enddef

  def set_date(self):

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
    self.date = (str(self.year_Chosen) + self.monthintchosen)   # creating a string for the date that is specific to what the user has selected
    print(self.date)
  #enddef

  def fetch_data(self):

    with open ("output.json", "r") as cf:   #  loading JSON file
      ojson = json.load(cf)

      for item in ojson['crimes']:
          
          if item['crimeType'] in self.crimelist: # only enters the next line if the crimeType of the current item matches one of the crimes in the crime list
              
              if item['location'] != 'No Location': # wont continue if there is no location for the cirime
                  
                  self.crimeCounter[item['crimeType']] += 1 #  increases the number associated with the crimeType of the current item by one
                  self.crimeid.append([item['crimeId']])

    for item in self.crimeCounter:

      if item in self.crimelist:
        print(f'{item}:  {self.crimeCounter[item]}') # printing the count for each chosen crime so that i can check
  #enddef



x = []

app = QApplication(sys.argv)

map = Map(x)
map.show()

window = SetUP()
window.show()

app.exec_()
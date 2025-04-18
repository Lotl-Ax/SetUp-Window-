from PyQt5 import uic, QtCore
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
    self.placeholders = [self.placeholder1, self.placeholder2, self.placeholder3, self.placeholder4, self.placeholder5, self.placeholder6, self.placeholder7, self.placeholder8, self.placeholder9, self.placeholder10, self.placeholder11, self.placeholder12]
    
    self.editSetup = self.findChild(QPushButton, 'Edit_Setup_Button')
    
    #setting event handlers
    self.editSetup.clicked.connect(self.open_setup)

  #enddef

  #Set of processes that use the data to assign each Crime to a Region

  # procedure that fetches the relevant data
  def fetch_data(self, date, crimes):
      crimesInfo = []  # list that will have tuples of relevant infomations
      crimeinfo = ()  # tuple that will be updated and added to the above list

      with open('output.json', 'r') as cf:
          ojson = json.load(cf)
          i = 0 

          for item in ojson['crimes']: # getting data that is relevant to the crimes the user wants and that have longitudes nad latitudes

              if item['latitude'] != "" and item['longitude'] != "": 
                    
                  if item['crimeType'] in crimes:
                      i += 1
                      crimeinfo = (item['crimeId'], item['longitude'], item['latitude']) # updating the tuple to have the Id, Longitude and Latitude of the current crime
                      crimesInfo.append(crimeinfo)  # adding the tuple to the list

      # overall map boundaries 
      low_lat = 50.86193  
      high_lat = 54.951083
      low_long = -0.000358
      high_long = 1.269397

      # getting the difference between the extremes of the boundaries
      lat_dif = high_lat - low_lat
      long_dif = high_long - low_long
      print(f'{lat_dif} \n{long_dif}')

      # dividing the difference in latitudes by the number of columns(3)
      lat_divd = lat_dif/3
      print(lat_divd)

      # dividing the difference in logitudes by the number of rows(4) 
      long_divd = long_dif/4
      print(long_divd)

      # setting the boundaries of each region based on the information above
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

      # dictionary of list refering to information in each region
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
      self.assign_to_region(Region_boundaries, RegionStore, crimesInfo) #sending relevant data to next procedure
  #enddef

  # procedure that assigns each crime to their region 
  def assign_to_region(self, Region_boundaries, RegionStore, crimesInfo):
    i = 0
    
    for item in crimesInfo: #getting and seperating the data from the tuples in crimesInfo(list)
        Id = item[0]
        Long = float(item[1])
        Lat = float(item[2])

        for region in Region_boundaries: # accessing the region boundaries of currrent region
            
            Reg_det = Region_boundaries[region]
            top = Reg_det['top']
            bottom = Reg_det['bottom']
            left = Reg_det['left']
            right = Reg_det['right']

            if Long >= left and Long <= right:
                if Lat <= top and Lat >= bottom: #assigning crime to specific region if longitude and latitude are within its given boundaries
                    i += 1
                    index = list(Region_boundaries).index(region)  # getting the index of the current Region we are in 
                    print(region, index)
                    list(RegionStore.values())[index].append(item)  # adding the current tuple to the relevant Region list in RegionStore

    self.display_region_vals(RegionStore)
  #enddef

  def display_region_vals(self, RegionStore):
      for i in RegionStore: # iterating through RegionStores lists
        print(i, RegionStore[i], len(RegionStore[i])) # displaying the Region, items in the list and length of list (for testing purposes)
        index = list(RegionStore).index(i)
        self.placeholders[index].setText(str(len(RegionStore[i]))) # setting the relevant placeholders Text to the length of the list

      self.show()
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
      self.set_date()
      self.hide()
      m = Map()
      m.fetch_data(self.date, self.crimelist)
      
      
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


app = QApplication(sys.argv)

window = SetUP()
window.show()

app.exec_()
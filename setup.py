from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox
import json 

import sys

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
      'Criminal daamage and arson':0,
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
      self.close()

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


app = QApplication(sys.argv)

window = SetUP()
window.show()
app.exec_()
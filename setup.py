from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox

import sys

class SetUP(QWidget):

  def __init__(self):
    
    super(SetUP, self).__init__()
    uic.loadUi("SetUP_widget.ui", self)

    self.setGeometry(750, 300, 650, 410)  # sets window position (750, 300) and its size w=600, h= 450
    self.setFixedSize(650, 410)  # fixes the window proportions so size cant be changed

    self.Robbery = self.findChild(QCheckBox, 'Robbery_Check')
    self.Arson = self.findChild(QCheckBox, 'Arson_Check')
    self.Crim_Dmg = self.findChild(QCheckBox, 'CrimDam_Check')
    self.Violence = self.findChild(QCheckBox, 'Violence_Check')
    self.Burglary = self.findChild(QCheckBox, 'Burglary_Check')
    self.FraudForge = self.findChild(QCheckBox, 'FandF_Check')
    self.SexualOffs = self.findChild(QCheckBox, 'SexOff_Check')
    self.Drugs = self.findChild(QCheckBox, 'Drugs_Check')
    self.TheftHandle = self.findChild(QCheckBox, 'TandH_Check')
    self.SelectAll = self.findChild(QCheckBox, 'SelectAL_Check')
    self.Save_btn = self.findChild(QPushButton, 'Save_Button')
    self.Safe = False # setting changes as unsaved, here as its connected to Save_btn
    self.Cont_btn = self.findChild(QPushButton, 'Continue_Button')
    self.Canc_btn = self.findChild(QPushButton, 'Cancel_Button')

    self.crimelist = []
    self.crimeSelected = 0

    #setting event handlers
    self.SelectAll.clicked.connect(self.Select_All)
    self.Robbery.stateChanged.connect(self.Robber_Select)
    self.Arson.stateChanged.connect(self.Arson_Select)
    self.Crim_Dmg.stateChanged.connect(self.CrimDmg_Select)
    self.Violence.stateChanged.connect(self.Violence_Select)
    self.Burglary.stateChanged.connect(self.Burglary_Select)
    self.FraudForge.stateChanged.connect(self.FandF_Select)
    self.SexualOffs.stateChanged.connect(self.SexualOffs_Select)
    self.Drugs.stateChanged.connect(self.Drug_Select)
    self.TheftHandle.stateChanged.connect(self.TheftHandle_Select)
    self.Save_btn.clicked.connect(self.Saved)
    self.Cont_btn.clicked.connect(self.Cont)
    self.Canc_btn.clicked.connect(self.Cancel)
    


    self.show()
  #enddef

  def NumCrimes_Selected(self, crime):
    

    if crime == True:

      self.crimeSelected += 1
      print(self.crimeSelected)

      if self.crimeSelected == 9:
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
      self.Arson.setChecked(True)
      self.Crim_Dmg.setChecked(True)
      self.Violence.setChecked(True)
      self.Burglary.setChecked(True)
      self.FraudForge.setChecked(True)
      self.SexualOffs.setChecked(True)
      self.Drugs.setChecked(True)
      self.TheftHandle.setChecked(True)

    else:
      self.Robbery.setChecked(False)
      self.Arson.setChecked(False)
      self.Crim_Dmg.setChecked(False)
      self.Violence.setChecked(False)
      self.Burglary.setChecked(False)
      self.FraudForge.setChecked(False)
      self.SexualOffs.setChecked(False)
      self.Drugs.setChecked(False)
      self.TheftHandle.setChecked(False)

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

  def Arson_Select(self):

    state = self.Arson.checkState()
    self.Safe = False

    if state == 2 :
      
      self.crimelist.append('Arson')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Arson')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def CrimDmg_Select(self):

    state = self.Crim_Dmg.checkState()
    self.Safe = False

    if state == 2:

      self.crimelist.append('Criminal Damage')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      print(self.crimelist)
      self.crimelist.remove('Criminal Damage')
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def Violence_Select(self):

    state = self.Violence.checkState()
    self.Safe = False

    if state == 2:
      
      self.crimelist.append('Violence')
      print(self.crimelist)
      self.NumCrimes_Selected(True)
    
    else:

      print(self.crimelist)
      self.NumCrimes_Selected(False)
      self.crimelist.remove('Violence')

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

  def FandF_Select(self):
    self.Safe =False
    state = self.FraudForge.checkState()

    if state == 2:

      self.crimelist.append('Fraud and Forgary')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Fraud and Forgary')
      print(self.crimelist)
      self.NumCrimes_Selected(False)

    #endif
  #enddef

  def SexualOffs_Select(self):
    self.Safe =False
    state = self.SexualOffs.checkState()

    if state == 2:

      self.crimelist.append('Sexual Offences')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.crimelist.remove('Sexual Offences')
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

  def TheftHandle_Select(self):
    self.Safe =False
    state = self.TheftHandle.checkState()

    if state == 2:

      self.crimelist.append('Theft and Handling')
      print(self.crimelist)
      self.NumCrimes_Selected(True)

    else:

      self.NumCrimes_Selected(False)
      self.crimelist.remove('Theft and Handling')
      print(self.crimelist)

    #endif
  #enddef

  def Saved(self):
    self.Safe = True  #  sets safe as True, essentially 'Saving' changes
    print('Saved:')
    print(self.crimelist)
  #endef

  def Cont(self):

      #  Checking Cont Method can access same variables as Save Mathod

    if self.Safe == True:
      self.close()

    else:

      msgbox = QMessageBox.warning(
        self,
        'HOLD ON',
        'Changes Are Not Saved! \nAre you sure you want to continue',
        QMessageBox.Yes | QMessageBox.No)

      if msgbox == QMessageBox.Yes:
        self.close()


  def Cancel(self):

    self.close()  #  closes the window




#1.  add function that adds a checked item to a list
#2.  add function that removes unchecked items from the list
#3.  add function that adds the month to a list
#4.  add function that adds the year to a list
#5. (3 and 4 probably dont need to be lists just variables)
#6.  add function that collects the chosen crimes and date when the Save Buttion is clicked 
  

app = QApplication(sys.argv)

window = SetUP()
window.show()
app.exec_()
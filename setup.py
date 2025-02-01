from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton

import sys

class SetUP(QMainWindow):

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


    #setting event handlers
    self.SelectAll.stateChanged.connect(self.Select_All)
    self.Robbery.stateChanged.connect(self.Robber_Select)
    self.Save_btn.clicked.connect(self.Saved)
    self.Cont_btn.clicked.connect(self.Cont)
    self.Canc_btn.clicked.connect(self.Cancel)


    self.show()
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

    if state == 2:
      print("Checked")
    
    else:
      print("unchecked")

    #endif
  #endef

  def Saved(self):
    self.Safe = True  #  sets safe as True, essentially 'Saving' changes
  #endef

  def Cont(self):

      #  Checking Cont Method can access same variables as Save Mathod

    if self.Safe == True:
      print("Cool")
      self.close()

    else:
      print("Not cool")
      self.newWin = Confirm()
  #enddef

  def Cancel(self):

    self.close()  #  closes the window






class Confirm(QMainWindow):
  
  def __init__(self):

    super(Confirm, self).__init__()
    uic.loadUi("Confirm_widget.ui", self)

    self.Confirm = self.findChild(QPushButton, 'Yes_confirm')
    self.Return = self.findChild(QPushButton, 'No_confirm')

    self.Confirm.clicked.connect(self.BothClose)
    self.Return.clicked.connect(self.ReturnSetUP)

    self.show()

  def BothClose(self):
    
    QMainWindow.close() #### Figure out how to close SetUP() on button click
    self.close()
    
  #enddef

  def ReturnSetUP(self):

    self.close()
  #enddef

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
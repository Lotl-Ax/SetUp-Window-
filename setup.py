from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox

import sys

class UI(QMainWindow):

  def __init__(self):
    
    super(UI, self).__init__()
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

    self.SelectAll.stateChanged.connect(self.Select_All)
    self.Robbery.stateChanged.connect(self.Robber_Select)


    self.show()


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

  def Robber_Select(self):

    state = self.Robbery.checkState()

    if state == 2:
      print("Checked")
    
    else:
      print("unchecked")



app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()
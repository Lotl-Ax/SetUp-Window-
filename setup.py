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

    self.SelectAll.stateChanged.connect(self.SelectedAll)



    def SelectedAll(self):
      state = self.SelectAll.checkState()

      if state == 2:
        self.Robbery.setState(True)
        self.Arson.setState(True)
        self.Crim_Dmg.setState(True)
        self.Violence.setState(True)
        self.Burglary.setState(True)
        self.FraudForge.setState(True)
        self.SexualOffs.setState(True)
        self.Drugs.setState(True)
        self.TheftHandle.setState(True)

      else:
        self.Robbery.setState(False)
        self.Arson.setState(False)
        self.Crim_Dmg.setState(False)
        self.Violence.setState(False)
        self.Burglary.setState(False)
        self.FraudForge.setState(False)
        self.SexualOffs.setState(False)
        self.Drugs.setState(False)
        self.TheftHandle.setState(False)


app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()
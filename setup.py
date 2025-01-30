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

    
app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import sys

class UI(QMainWindow):

  def __init__(self):
    
    super(UI, self).__init__()
    uic.loadUi("SetUP.ui", self)

app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()
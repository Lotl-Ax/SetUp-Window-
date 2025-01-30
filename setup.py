from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

import sys

class UI(QMainWindow):

  def __init__(self):
    
    super(UI, self).__init__()
    uic.loadUi("SetUP_widget.ui", self)

    self.setGeometry(750, 300, 700, 500)  # sets window position (750, 300) and its size w=600, h= 450
    #self.setFixedSize(600, 450)  # fixes the window proportions so size cant be changed

app = QApplication(sys.argv)

window = UI()
window.show()
app.exec_()
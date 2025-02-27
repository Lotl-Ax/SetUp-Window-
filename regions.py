from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QGraphicsView

import sys

class Map(QMainWindow):

  def __init__(self):
    
    super(Map, self).__init__()
    uic.loadUi("Wireframe.ui", self)

    self.Graphics = self.findChild(QGraphicsView, 'graphicsView')
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

    # Regions will be given specific longitude and latitude boundaries where i plan on adding crime items that fit within each Region
    # Lontide decrease left (<--) and increases right (-->)
    # Latitude increases up and decreases down
    # so top left (region 1/ placeholder 1) must have highest latitude option and lowest Lontitude option ( to other spcified location)
    # and bottom right must have lowest latitude and hightest longitude options
    Region_1 = []
    Region_2 = ['a', 'b', 'c']
    Region_3 = ['a', 'b', 'c', 'd', 'e']
    Region_4 = ['a', 'b']
    Region_5 = ['a', 'b', 'c', 'd', 'e']

    mark_1_text = str(len(Region_1))
    mark_2_text = str(len(Region_2))
    mark_3_text = str(len(Region_3))
    mark_4_text = str(len(Region_4))
    mark_5_text = str(len(Region_5))

    self.placeholder1.setText('1')
    self.placeholder2.setText('2')
    self.placeholder3.setText('3')
    self.placeholder4.setText('4')
    self.placeholder5.setText('5')
    self.placeholder6.setText('6')
    self.placeholder7.setText('7')
    self.placeholder8.setText('8')
    self.placeholder9.setText('9')
    self.placeholder10.setText('10')
    self.placeholder11.setText('11')
    self.placeholder12.setText('12')





app = QApplication(sys.argv)

window = Map()
window.show()
app.exec_()
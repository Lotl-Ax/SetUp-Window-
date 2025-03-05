import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QGraphicsView

import sys

low_lat = 50.86193
high_lat = 54.951083
low_long = -0.000358
high_long = 1.269397

lat_dif = high_lat - low_lat
long_dif = high_long - low_long

mid_lat_dif = lat_dif/2
centre_lat = low_lat+mid_lat_dif

mid_long_dif = long_dif/2
centre_long = low_long + mid_long_dif

print(f'centre: {centre_lat},{centre_long}')
print(f'topleft: {high_lat},{low_long}')
print(f'bttmRght: {low_lat},{high_long}')



#52.9065065
#0.6345195000000001
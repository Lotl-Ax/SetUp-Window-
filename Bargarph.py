import matplotlib.pyplot as Mplt
import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QMessageBox, QComboBox, QLabel, QGroupBox, QTabWidget
import sys

class Map(QMainWindow):

    def __init__(self):
    
        super(Map, self).__init__()
        uic.loadUi("Wireframe.ui", self)

        self.Tab = self.findChild(QTabWidget, 'Tabs')
        self.bar_preview = self.findChild(QGroupBox, 'bar_graph_preview')
        self.line_preview = self.findChild(QGroupBox, 'line_graph_preview')
        self.pie_preview = self.findChild(QGroupBox, 'pie_chart_preview')
        self.popu_preview = self.findChild(QGroupBox, 'pop_graph_preview')
        graph_previews = self.bar_preview = self.line_preview = self.pie_preview = self.popu_preview
        graph_previews.setTitle('') 

        self.crime = ['Anti-social behaviour', 'Bicycle theft', 'Burglary', 'Criminal damage and arson', 'Drugs', 'Possession of weapons', 'Public order', 'Robbery', 'Shoplifting', 'Theft from the person', 'Vehicle crime', 'Violence and sexual offences']
        self.amount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        self.show()

    def set_bar_preview_data(self):

        with open ("output.json", "r") as cf:   #  loading JSON file
            ojson = json.load(cf)
            
            for item in ojson['crimes']:
                
                if item['crimeType'] in self.crime: 
                    this_crime = item['crimeType']
                    index = self.crime.index(this_crime)
                    self.amount[index] += 1
                #endif
            #endfor
        #endwith
        self.get_bar_preview()
    #enddef

    def get_bar_preview(self):

        font = {'family':'serif','color':'darkred','size':10}

        Mplt.barh(self.crime, self.amount, height=0.5, color=['blue', 'green'])

        Mplt.ylabel('Crime', fontdict=font)
        Mplt.xlabel('Amount', fontdict=font)

        Mplt.title('Crime amounts')

        Mplt.tight_layout()

        Mplt.show()
        
    #enddef
    


app = QApplication(sys.argv)

map = Map()
map.show()

app.exec_()

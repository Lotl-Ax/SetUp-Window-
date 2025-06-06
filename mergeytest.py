import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QTabWidget, QLabel)
from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGroupBox, QPushButton, QMessageBox, QComboBox, QLabel
import json 
from PyQt5.QtGui import QPainter

        
class Map(QMainWindow):

  def __init__(self):
    
    super(Map, self).__init__()
    uic.loadUi("Wireframe.ui", self)

    self.Graphics = self.findChild(QLabel, 'Image')
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
    self.placeholders = [self.placeholder1, self.placeholder2, self.placeholder3, self.placeholder4, self.placeholder5, self.placeholder6, self.placeholder7, self.placeholder8, self.placeholder9, self.placeholder10, self.placeholder11, self.placeholder12]
    
    self.BarView = self.findChild(QGroupBox, 'bar_graph_preview')

    self.editSetup = self.findChild(QPushButton, 'Edit_Setup_Button')
    

  #enddef

  #Set of processes that use the data to assign each Crime to a Region

  # procedure that fetches the relevant data
  def fetch_parameters(self, crimes, date):

    self.crimes = crimes
    self.date = date
    print(f'recieved {self.crimes, self.date}')
    self.fetch_data()
  #enddef

  def fetch_data(self):
      crimes = self.crimes
      date = self.date

      crimesInfo = []  # list that will have tuples of relevant infomations
      crimeinfo = ()  # tuple that will be updated and added to the above list

      with open('output.json', 'r') as cf:
          ojson = json.load(cf)
          i = 0 

          for item in ojson['crimes']: # getting data that is relevant to the crimes the user wants and that have longitudes nad latitudes

              if item['latitude'] != "" and item['longitude'] != "": 
                    
                  if item['crimeType'] in crimes:
                      i += 1
                      crimeinfo = (item['crimeId'], item['longitude'], item['latitude']) # updating the tuple to have the Id, Longitude and Latitude of the current crime
                      crimesInfo.append(crimeinfo)  # adding the tuple to the list

      # overall map boundaries 
      low_lat = 50.86193  
      high_lat = 54.951083
      low_long = -0.000358
      high_long = 1.269397

      # getting the difference between the extremes of the boundaries
      lat_dif = high_lat - low_lat
      long_dif = high_long - low_long
      print(f'{lat_dif} \n{long_dif}')

      # dividing the difference in latitudes by the number of columns(3)
      lat_divd = lat_dif/3
      print(lat_divd)

      # dividing the difference in logitudes by the number of rows(4) 
      long_divd = long_dif/4
      print(long_divd)

      # setting the boundaries of each region based on the information above
      Region_boundaries = {
          'Region_1_boundaries' : {
                  'top':high_lat,
                  'bottom':(high_lat-lat_divd),
                  'left':low_long,
                  'right':(low_long+long_divd)
              } ,

              'Region_2_boundaries' : {
                  'top':(high_lat-lat_divd),
                  'bottom':(low_lat + lat_divd),
                  'left':low_long,
                  'right':(low_long+long_divd)
              } ,

              'Region_3_boundaries' : {
                  'top':(low_lat + lat_divd),
                  'bottom':low_lat,
                  'left':low_long,
                  'right':(low_long+long_divd)
              },

              'Region_4_boundaries' : {
                  'top':high_lat,
                  'bottom':(high_lat-lat_divd),
                  'left':(low_long+long_divd),
                  'right':(low_long+long_divd+long_divd)
              } ,

              'Region_5_boundaries': {
                  'top':(high_lat-lat_divd),
                  'bottom':(low_lat + lat_divd),
                  'left':(low_long+long_divd),
                  'right':(low_long+long_divd+long_divd)
              },

              'Region_6_boundaries' : {
                  'top':(low_lat + lat_divd),
                  'bottom':low_lat,
                  'left':(low_long+long_divd),
                  'right':(low_long+long_divd+long_divd)
              },

              'Region_7_boundaries' : {
                  'top':high_lat,
                  'bottom':(high_lat-lat_divd),
                  'left':(high_long-long_divd-long_divd),
                  'right':(high_long-long_divd)
              },

              'Region_8_boundaries' : {
                  'top':(high_lat-lat_divd),
                  'bottom':(low_lat + lat_divd),
                  'left':(high_long-long_divd-long_divd),
                  'right':(high_long-long_divd)
              },

              'Region_9_boundaries' : {
                  'top':(low_lat + lat_divd),
                  'bottom':low_lat,
                  'left':(high_long-long_divd-long_divd),
                  'right':(high_long-long_divd)
              },

              'Region_10_boundaries' : {
                  'top':high_lat,
                  'bottom':(high_lat-lat_divd),
                  'left':(high_long-long_divd),
                  'right':high_long
              },

              'Region_11_boundaries' : {
                  'top':(high_lat-lat_divd),
                  'bottom':(low_lat + lat_divd),
                  'left':(high_long-long_divd),
                  'right':high_long
              },

              'Region_12_boundaries' : {
                  'top':(low_lat + lat_divd),
                  'bottom':low_lat,
                  'left':(high_long-long_divd),
                  'right':high_long
              }
      }

      # dictionary of list refering to information in each region
      RegionStore  = {
          'Reg1' : [],
          'Reg2' : [],
          'Reg3' : [],
          'Reg4' : [],
          'Reg5' : [],
          'Reg6' : [],
          'Reg7' : [],
          'Reg8' : [],
          'Reg9' : [],
          'Reg10' : [],
          'Reg11' : [],
          'Reg12' : [],
      }

      print(i)
      self.assign_to_region(Region_boundaries, RegionStore, crimesInfo) #sending relevant data to next procedure
  #enddef

  # procedure that assigns each crime to their region 
  def assign_to_region(self, Region_boundaries, RegionStore, crimesInfo):
    i = 0
    
    for item in crimesInfo: #getting and seperating the data from the tuples in crimesInfo(list)
        Id = item[0]
        Long = float(item[1])
        Lat = float(item[2])

        for region in Region_boundaries: # accessing the region boundaries of currrent region
            
            Reg_det = Region_boundaries[region]
            top = Reg_det['top']
            bottom = Reg_det['bottom']
            left = Reg_det['left']
            right = Reg_det['right']

            if Long >= left and Long <= right:
                if Lat <= top and Lat >= bottom: #assigning crime to specific region if longitude and latitude are within its given boundaries
                    i += 1
                    index = list(Region_boundaries).index(region)  # getting the index of the current Region we are in 
                    print(region, index)
                    list(RegionStore.values())[index].append(item)  # adding the current tuple to the relevant Region list in RegionStore

    self.display_region_vals(RegionStore)
  #enddef

  def display_region_vals(self, RegionStore):
      for i in RegionStore: # iterating through RegionStores lists
        print(i, RegionStore[i], len(RegionStore[i])) # displaying the Region, items in the list and length of list (for testing purposes)
        index = list(RegionStore).index(i)
        self.placeholders[index].setText(str(len(RegionStore[i]))) # setting the relevant placeholders Text to the length of the list

      self.show()
  #enddef



class BarGraph(QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        set0 = QBarSet('X0')

        set0.append([56, 558, 285, 410, 2342, 57, 42, 156, 569, 131, 301, 889])
		
        series = QHorizontalBarSeries()
        series.append(set0)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Crime Prevalance')
        
        chart.setAnimationOptions(QChart.SeriesAnimations)
		
            # words appear top to bottom
        crimes = ('Possession of Weapons', 'Public Order', 'Shoplifting', 'Vehicle crime', 'Violence and sexual offences', 'Theft from the person', 'Robbery', 'Drugs', 'Criminal damage and arson', 'Bicycle theft', 'Burglary', 'Anti-social behaviour')

        axisY = QBarCategoryAxis()
        axisY.append(crimes)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        axisX = QValueAxis()
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisX.applyNiceNumbers()

        chart.legend().setVisible(False)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.show()


    
app = QApplication(sys.argv)

window = Map()
window.show()
app.exec_()
import sys
import pyqtgraph as pg
from PyQt5 import uic, QtCore, QtGui
from PyQt5 import QtChart, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QMdiArea, QMdiSubWindow, QApplication, QAction, QLCDNumber

class Window(QtWidgets.QMainWindow):  # Window that is produced from the toolbar

    def __init__(self):
        super().__init__()

        self.setGeometry(750, 300, 760, 410)

        self.vertical_layout = QtWidgets.QVBoxLayout(self)

        self.set1 = QtChart.QBarSet('Room 1')

        room_1 = {'Burglary':50, 'Arson':204, 'Cats':90}

        self.set1.append(room_1.values())

        self.bar_series = QtChart.QBarSeries()
        self.bar_series.append(self.set1)

        self.chart = QtChart.QChart()
        self.chart.addSeries(self.bar_series)

        self.categories = ['Burglary', 'Arson', 'Cats']
        self.x_axis = QtChart.QBarCategoryAxis()
        self.x_axis.append(self.categories)
        self.chart.setAxisX(self.x_axis, self.bar_series)

        self.y_axis = QtChart.QValueAxis()
        self.chart.setAxisY(self.y_axis, self.bar_series)
        self.y_axis.setRange(0,30)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(QtCore.Qt.AlignTop)
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        self.chart_view = QtChart.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

        self.vertical_layout.addWidget(self.chart_view)

# main starts here
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()

    app.exec_()

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QTabWidget, QLabel)
from PyQt5.QtChart import QChart, QChartView, QHorizontalBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter


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

window = BarGraph()
window.show()
app.exec_()
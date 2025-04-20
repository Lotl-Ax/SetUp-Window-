import sys, random
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)

		set0 = QBarSet('X0')

		set0.append([889, 301, 131, 569, 156, 42, 57, 2342, 410, 285, 503, 184, 558, 56])

		series = QBarSeries()
		series.append(set0)
		
		chart = QChart()
		chart.addSeries(series)
		chart.setTitle('Crime Amounts')
		chart.setAnimationOptions(QChart.SeriesAnimations)

		months = ('Anti-social behaviour', 'Burglary', 'Bicycle theft', 'Criminal damage and arson', 'Drugs', 'Robbery', 'Theft from the person', 'Violence and sexual offences', ' Vehicle crime', 'Shoplifting', 'Other theft', 'Other crime', 'Public order', 'Possesssionof weapons')

		axisX = QBarCategoryAxis()
		axisX.append(months)

		axisY = QValueAxis()
		axisY.setRange(0, 2342)

		chart.addAxis(axisX, Qt.AlignBottom)
		chart.addAxis(axisY, Qt.AlignLeft)

		chart.legend().setVisible(False)

		chartView = QChartView(chart)
		self.setCentralWidget(chartView)

if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec_())
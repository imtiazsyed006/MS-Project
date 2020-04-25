## This can be used for showing Yaw, Pitch and Roll

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import os
import numpy as np
import math
import time

firstRun = []
data = np.linspace(0,2*math.pi,60)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(39, 29, 721, 531))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.y = [0,0]
        self.x = [0,0]
        self.y1 = [0,0]
        self.x1 = [0,0]
        self.widget.  setYRange(-10,10)
        self.widget.  setXRange(-10,10)
        self.widget.showGrid(x = True,y = True)

        self.data_line = self.widget.plot(self.x,self.y,symbol = 'o')
        self.data_line1 = self.widget.plot(self.x1,self.y1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def update_plot_data(self):
    	if not firstRun:
    		global i 
    		global j
    		j = 0
    		i = 0
    		firstRun.append(1)

    	self.x[0] = 0
    	self.x[1] = 10*math.cos(data[i])
    	self.y[0] = 0
    	self.y[1] = 10*math.sin(data[i])
    	self.data_line.setData(self.x,self.y)
    	i = i+1
    	if j == 0:
    		self.x1[0] = 0
    		self.x1[1] = 5*math.cos(data[j])
    		self.y1[0] = 0
    		self.y1[1] = 5*math.sin(data[j])
    		self.data_line1.setData(self.x1,self.y1)
    		j = j + 1
    	if i == 60:
    		i = 0
    		self.x1[0] = 0
	    	self.x1[1] = 5*math.cos(data[j])
	    	self.y1[0] = 0
	    	self.y1[1] = 5*math.sin(data[j])
	    	j = j + 1
	    	if j == 60:
	    		j = 0
	    	self.data_line1.setData(self.x1,self.y1)
	    	


    		

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

## The very first attempt to plot real time data in PyQt5 using PyQtGraph

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg # We need sys so that we can pass argv to QApplication
import os
import numpy as np
import Adxl345_1 as adxl


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(19, 19, 761, 191))
        self.widget.setObjectName("widget")

        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(20, 290, 761, 191))
        self.widget_2.setObjectName("widget_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##        self.x = list(range(100))  # 100 time points
##        self.y = [np.random.randint(0,100) for _ in range(100)]  # 100 data points

        self.x = []
##        self.y = []
##        self.z = []
        self.t = []
        self.firstRun = []
        self.firstRun1 = []
        self.widget.setBackground('w')
        self.widget.setYRange(-1,1)
        self.widget.setTitle('Plot # 01')
        self.widget.setLabel('left','Y axis')
        self.widget.setLabel('bottom','X axis')
        self.widget.showGrid(x = True, y = True)
        

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.widget.plot(self.t, self.x, pen=pen)

##        self.plot_1([1,2,3,4],[1,2,3,4])
##        self.plot_2([1,4,8,16],[1,2,3,4])

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

##    def plot_1(self,a,b):
##        self.widget.plot(a,b)
##        self.widget.setTitle('Plot # 01')
##        self.widget.setLabel('left','Y axis')
##        self.widget.setLabel('bottom','X axis')
##        self.widget.showGrid(x = True, y = True)
##
##    def plot_2(self,a,b):
##        self.widget_2.plot(a,b)

##    def update_plot_data(self):

##        self.x = self.x[1:]  # Remove the first y element.
##        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
##
##        self.y = self.y[1:]  # Remove the first 
##        self.y.append(np.random.randint(0,100))  # Add a new random value.
##
##        self.data_line.setData(self.x, self.y)   # Update the data.

    def update_plot_data(self):
        if len(self.firstRun) <= 50:
            self.firstRun.append(1)
            self.t = np.arange(1,len(self.firstRun)+1)
            self.xi,self.yi,self.zi = adxl.adxlfor()
            self.x.append(self.xi)
            self.data_line.setData(self.t,self.x)

        else:
            if not self.firstRun1:
                self.t = list(self.t)
                self.firstRun1.append(1)
                self.t = self.t[1:]
                self.t.append(self.t[-1]+1)
                xi,yi,zi = adxl.adxlfor()
                self.x = self.x[1:]
                self.x.append(xi)
                self.data_line.setData(self.t,self.x)
             
            self.t = self.t[1:]
            self.t.append(self.t[-1]+1)
            xi,yi,zi = adxl.adxlfor()
            self.x = self.x[1:]
            self.x.append(xi)
            self.data_line.setData(self.t,self.x)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

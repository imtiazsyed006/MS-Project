from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import matplotlib.pyplot as plt
import ADXL345 as adxl345
from drawnow import*
import numpy as np
from PyQt5.QtCore import QTimer

angleFaccel = []



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(270, 200, 191, 151))
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber1.setGeometry(QtCore.QRect(0, 0, 191, 151))
        self.lcdNumber1.setObjectName("lcdNumber")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def get_value(self):
        a,b,c = adxl345.Get_ADXL345_Values()
        angleFaccel.append(int(a))
        self.lcdNumber.display(angleFaccel[-1])

    def get_value1(self):
        self.lcdNumber1.display(angleFaccel[-1])
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    def update():
        ui.get_value()
        
    def update1():
        ui.get_value1()
        
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(100)

    timer1 = QtCore.QTimer()
    timer1.timeout.connect(update1)
    timer1.start(1000)
    
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import os
import numpy as np
import Adxl345_1 as adxl
import time
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ledPin = 32

GPIO.setup(ledPin, GPIO.OUT,initial = GPIO.LOW)
p = GPIO.PWM(ledPin, 1000)
p.start(0)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 256, 144))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setAcceptDrops(False)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = PlotWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 144, 256, 144))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = PlotWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 288, 256, 144))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = PlotWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 432, 256, 144))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = PlotWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 576, 256, 144))
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = PlotWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(256, 0, 256, 144))
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = PlotWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(512, 0, 256, 144))
        self.widget_7.setObjectName("widget_7")
        self.widget_8 = PlotWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(768, 0, 256, 144))
        self.widget_8.setObjectName("widget_8")
        self.widget_9 = PlotWidget(self.centralwidget)
        self.widget_9.setGeometry(QtCore.QRect(1024, 0, 256, 144))
        self.widget_9.setObjectName("widget_9")
        ##
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(600, 400, 300, 100))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged[int].connect(self.changeValue)
        ##
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(600, 300, 300, 100))
        self.lcdNumber.setObjectName("lcdNumber")
        ##
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(600, 500, 161, 101))
        self.checkBox.stateChanged.connect(self.logData)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(24, 24))
        self.checkBox.setObjectName("checkBox")
        ##
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1024, 180, 256, 51))
        ##
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1060, 250, 50, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1060, 270, 50, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1060, 290, 50, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1120, 270, 50, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1120, 250, 50, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1120, 290, 50, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1190, 270, 50, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1190, 250, 50, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1190, 290, 50, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1190, 370, 50, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1060, 350, 50, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1120, 350, 50, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1120, 330, 50, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1060, 330, 50, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1060, 370, 50, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1120, 370, 50, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1190, 330, 50, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1190, 350, 50, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1190, 450, 50, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1060, 430, 50, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1120, 430, 50, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1120, 410, 50, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1060, 410, 50, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1060, 450, 50, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1120, 450, 50, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1190, 410, 50, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(1190, 430, 50, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1190, 530, 50, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1060, 510, 50, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1120, 510, 50, 16))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1120, 490, 50, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1060, 490, 50, 16))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1060, 530, 50, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(1120, 530, 50, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(1190, 490, 50, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(1190, 510, 50, 16))
        self.label_37.setObjectName("label_37")
        ##
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setGeometry(QtCore.QRect(1020, 240, 256, 411))
        self.widget_10.setStyleSheet("")
        self.widget_10.setObjectName("widget_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        self.x = []
        self.t = []
        self.firstRun = []
        self.firstRun1 = []
        self.fileName = ''
##        self.widget.setBackground('w')
        self.widget.  setYRange(-1,1)
        self.widget_2.setYRange(-1,1)
        self.widget_3.setYRange(-1,1)
        self.widget_4.setYRange(-1,1)
        self.widget_5.setYRange(-1,1)
        self.widget_6.setYRange(-1,1)
        self.widget_7.setYRange(-1,1)
        self.widget_8.setYRange(-1,1)
        self.widget_9.setYRange(-1,1)
        
        font2=QtGui.QFont()
        font2.setPixelSize(11)
        pen = pg.mkPen(color=(255, 0, 0), width = 1)
        
        self.widget.  setTitle('X vs Y',size = '10px')
        self.widget_2.setTitle('X vs Y',size = '10px')
        self.widget_3.setTitle('X vs Y',size = '10px')
        self.widget_4.setTitle('X vs Y',size = '10px')
        self.widget_5.setTitle('X vs Y',size = '10px')
        self.widget_6.setTitle('X vs Y',size = '10px')
        self.widget_7.setTitle('X vs Y',size = '10px')
        self.widget_8.setTitle('X vs Y',size = '10px')
        self.widget_9.setTitle('X vs Y',size = '10px')
        
        #labelStyle = {'color': '#008000', 'font-size': '10px'}
        ##self.widget.setLabel('bottom','X axis',**labelStyle)
        ##self.widget.setLabel('left'  ,'Y axis',**labelStyle)
        
        self.widget.showGrid  (x = True, y = True)
        self.widget_2.showGrid(x = True, y = True)
        self.widget_3.showGrid(x = True, y = True)
        self.widget_4.showGrid(x = True, y = True)
        self.widget_5.showGrid(x = True, y = True)
        self.widget_6.showGrid(x = True, y = True)
        self.widget_7.showGrid(x = True, y = True)
        self.widget_8.showGrid(x = True, y = True)
        self.widget_9.showGrid(x = True, y = True)
        
        self.widget.getAxis("left").    tickFont = font2
        self.widget.getAxis("bottom").  tickFont = font2
        self.widget_2.getAxis("left").  tickFont = font2
        self.widget_2.getAxis("bottom").tickFont = font2
        self.widget_3.getAxis("left").  tickFont = font2
        self.widget_3.getAxis("bottom").tickFont = font2
        self.widget_4.getAxis("left").  tickFont = font2
        self.widget_4.getAxis("bottom").tickFont = font2
        self.widget_5.getAxis("left").  tickFont = font2
        self.widget_5.getAxis("bottom").tickFont = font2
        self.widget_6.getAxis("left").  tickFont = font2
        self.widget_6.getAxis("bottom").tickFont = font2
        self.widget_7.getAxis("left").  tickFont = font2
        self.widget_7.getAxis("bottom").tickFont = font2
        self.widget_8.getAxis("left").  tickFont = font2
        self.widget_8.getAxis("bottom").tickFont = font2
        self.widget_9.getAxis("left").  tickFont = font2
        self.widget_9.getAxis("bottom").tickFont = font2
        
        ##self.widget.getAxis("left").setStyle(tickTextOffset = 1)
        
        self.data_line   =  self.widget.plot  (self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_1 =  self.widget_2.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_2 =  self.widget_3.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_3 =  self.widget_4.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_4 =  self.widget_5.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_5 =  self.widget_6.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_6 =  self.widget_7.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_7 =  self.widget_8.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        self.data_line_8 =  self.widget_9.plot(self.t, self.x, pen=pen,fillLevel = 0,fillBrush = (255,255,255,50))
        
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(10)
        self.timer2.timeout.connect(self.updateLed)
        self.timer2.start()

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Raw Telemetry Data"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_2.setText(_translate("MainWindow", "g_x"))
        self.label_3.setText(_translate("MainWindow", "g_y"))
        self.label_4.setText(_translate("MainWindow", "g_z"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "m/s2"))
        self.label_9.setText(_translate("MainWindow", "m/s2"))
        self.label_10.setText(_translate("MainWindow", "m/s2"))
        self.label_11.setText(_translate("MainWindow", "m/s2"))
        self.label_12.setText(_translate("MainWindow", "g_y"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "g_x"))
        self.label_16.setText(_translate("MainWindow", "g_z"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "m/s2"))
        self.label_19.setText(_translate("MainWindow", "m/s2"))
        self.label_20.setText(_translate("MainWindow", "m/s2"))
        self.label_21.setText(_translate("MainWindow", "g_y"))
        self.label_22.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "g_x"))
        self.label_25.setText(_translate("MainWindow", "g_z"))
        self.label_26.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "m/s2"))
        self.label_28.setText(_translate("MainWindow", "m/s2"))
        self.label_29.setText(_translate("MainWindow", "m/s2"))
        self.label_30.setText(_translate("MainWindow", "g_y"))
        self.label_31.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "g_x"))
        self.label_34.setText(_translate("MainWindow", "g_z"))
        self.label_35.setText(_translate("MainWindow", "0"))
        self.label_36.setText(_translate("MainWindow", "m/s2"))
        self.label_37.setText(_translate("MainWindow", "m/s2"))

    def update_plot_data(self):
        if len(self.firstRun) <= 20:
            if not self.fileName:
                self.firstRun.append(1)
                self.t = np.arange(1,len(self.firstRun)+1)
                self.xi,self.yi,self.zi = adxl.adxlfor()
                self.x.append(self.xi)
                self.data_line.setData(self.t,self.x)
                self.data_line_1.setData(self.t,self.x)
                self.data_line_2.setData(self.t,self.x)
                self.data_line_3.setData(self.t,self.x)
                self.data_line_4.setData(self.t,self.x)
                self.data_line_5.setData(self.t,self.x)
                self.data_line_6.setData(self.t,self.x)
                self.data_line_7.setData(self.t,self.x)
                self.data_line_8.setData(self.t,self.x)
                self.changeLabelText(self.xi)
            else:
                self.firstRun.append(1)
                self.t = np.arange(1,len(self.firstRun)+1)
                self.xi,self.yi,self.zi = adxl.adxlfor()
                self.x.append(self.xi)
                self.data_line.setData(self.t,self.x)
                self.data_line_1.setData(self.t,self.x)
                self.data_line_2.setData(self.t,self.x)
                self.data_line_3.setData(self.t,self.x)
                self.data_line_4.setData(self.t,self.x)
                self.data_line_5.setData(self.t,self.x)
                self.data_line_6.setData(self.t,self.x)
                self.data_line_7.setData(self.t,self.x)
                self.data_line_8.setData(self.t,self.x)
                self.changeLabelText(self.xi)
                with open(self.fileName+'.txt','a') as file:
                    file.write(str(xi)+','+str(yi)+','+str(zi)+'\n')
           
        else:
            if not self.firstRun1:
                if not self.fileName:
                    self.t = list(self.t)
                    self.firstRun1.append(1)
                    self.t = self.t[1:]
                    self.t.append(self.t[-1]+1)
                    xi,yi,zi = adxl.adxlfor()
                    self.x = self.x[1:]
                    self.x.append(xi)
                    self.data_line.setData(self.t,self.x)
                    self.data_line_1.setData(self.t,self.x)
                    self.data_line_2.setData(self.t,self.x)
                    self.data_line_3.setData(self.t,self.x)
                    self.data_line_4.setData(self.t,self.x)
                    self.data_line_5.setData(self.t,self.x)
                    self.data_line_6.setData(self.t,self.x)
                    self.data_line_7.setData(self.t,self.x)
                    self.data_line_8.setData(self.t,self.x)
                    self.changeLabelText(xi)
                else:
                    self.t = list(self.t)
                    self.firstRun1.append(1)
                    self.t = self.t[1:]
                    self.t.append(self.t[-1]+1)
                    xi,yi,zi = adxl.adxlfor()
                    self.x = self.x[1:]
                    self.x.append(xi)
                    self.data_line.setData(self.t,self.x)
                    self.data_line_1.setData(self.t,self.x)
                    self.data_line_2.setData(self.t,self.x)
                    self.data_line_3.setData(self.t,self.x)
                    self.data_line_4.setData(self.t,self.x)
                    self.data_line_5.setData(self.t,self.x)
                    self.data_line_6.setData(self.t,self.x)
                    self.data_line_7.setData(self.t,self.x)
                    self.data_line_8.setData(self.t,self.x)
                    self.changeLabelText(xi)
                    with open(self.fileName+'.txt','a') as file:
                        file.write(str(xi)+','+str(yi)+','+str(zi)+'\n')
                
            if not self.fileName:
                self.t = self.t[1:]
                self.t.append(self.t[-1]+1)
                xi,yi,zi = adxl.adxlfor()
                self.x = self.x[1:]
                self.x.append(xi)
                self.data_line.setData(self.t,self.x)
                self.data_line_1.setData(self.t,self.x)
                self.data_line_2.setData(self.t,self.x)
                self.data_line_3.setData(self.t,self.x)
                self.data_line_4.setData(self.t,self.x)
                self.data_line_5.setData(self.t,self.x)
                self.data_line_6.setData(self.t,self.x)
                self.data_line_7.setData(self.t,self.x)
                self.data_line_8.setData(self.t,self.x)
                self.changeLabelText(xi)
                
            else:
                self.t = self.t[1:]
                self.t.append(self.t[-1]+1)
                xi,yi,zi = adxl.adxlfor()
                self.x = self.x[1:]
                self.x.append(xi)
                self.data_line.setData(self.t,self.x)
                self.data_line_1.setData(self.t,self.x)
                self.data_line_2.setData(self.t,self.x)
                self.data_line_3.setData(self.t,self.x)
                self.data_line_4.setData(self.t,self.x)
                self.data_line_5.setData(self.t,self.x)
                self.data_line_6.setData(self.t,self.x)
                self.data_line_7.setData(self.t,self.x)
                self.data_line_8.setData(self.t,self.x)
                self.changeLabelText(xi)
                with open(self.fileName+'.txt','a') as file:
                    file.write(str(xi)+','+str(yi)+','+str(zi)+'\n')

    def updateLed(self):
        value = self.horizontalSlider.value()
        p.ChangeDutyCycle(value)

    def changeValue(self,value):
        print(value)
        self.pwm = [value]
        self.lcdNumber.display(value)

    def logData(self,state):
        
        if state == QtCore.Qt.Checked:
            year   = time.localtime().tm_year
            month  = time.localtime().tm_mon
            day    = time.localtime().tm_mday
            hour   = time.localtime().tm_hour
            minute = time.localtime().tm_min
            second = time.localtime().tm_sec
            print('Data logging started')
            self.fileName = str(year)+'_'+str(month)+'_'+str(day)+'_'+str(hour)+'_'+str(minute)+'_'+str(second)
            # with open(fileName + str('.txt'),'a') as file:
            #     file.write(str(1)+'\n')

        else:
            self.fileName = ''
            print('Data logging stopped')

    def changeLabelText(self,a):
        self.label_5.setText(str(round(a,3)))
        self.label_6.setText(str(round(a,3)))
        self.label_7.setText(str(round(a,3)))
        self.label_13.setText(str(round(a,3)))
        self.label_14.setText(str(round(a,3)))
        self.label_17.setText(str(round(a,3)))
        self.label_22.setText(str(round(a,3)))
        self.label_23.setText(str(round(a,3)))
        self.label_26.setText(str(round(a,3)))
        self.label_31.setText(str(round(a,3)))
        self.label_32.setText(str(round(a,3)))
        self.label_35.setText(str(round(a,3)))
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

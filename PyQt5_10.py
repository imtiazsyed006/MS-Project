from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import os
import numpy as np
import Adxl345_1 as adxl


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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1024, 180, 256, 51))
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
        self.x2 = []
        self.x3 = []
        self.x4 = []
        self.x5 = []
        self.x6 = []
        self.x7 = []
        self.x8 = []
        self.x9 = []
        
        self.t = []
        self.firstRun = []
        self.firstRun1 = []
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
        
        self.data_line   =  self.widget.plot  (self.t, self.x, pen=pen)
        self.data_line_1 =  self.widget_2.plot(self.t, self.x2, pen=pen)
        self.data_line_2 =  self.widget_3.plot(self.t, self.x3, pen=pen)
        self.data_line_3 =  self.widget_4.plot(self.t, self.x4, pen=pen)
        self.data_line_4 =  self.widget_5.plot(self.t, self.x5, pen=pen)
        self.data_line_5 =  self.widget_6.plot(self.t, self.x6, pen=pen)
        self.data_line_6 =  self.widget_7.plot(self.t, self.x7, pen=pen)
        self.data_line_7 =  self.widget_8.plot(self.t, self.x8, pen=pen)
        self.data_line_8 =  self.widget_9.plot(self.t, self.x9, pen=pen)
        
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Raw Telemetry Data"))

    def update_plot_data(self):
        if len(self.firstRun) <= 10:
            self.firstRun.append(1)
            self.t = np.arange(1,len(self.firstRun)+1)
            self.xi,self.yi,self.zi = adxl.adxlfor()
            self.x.append(self.xi)
            self.x2.append(self.xi)
            self.x3.append(self.xi)
            self.x4.append(self.xi)
            self.x5.append(self.xi)
            self.x6.append(self.xi)
            self.x7.append(self.xi)
            self.x8.append(self.xi)
            self.x9.append(self.xi)
            
            self.data_line.setData(self.t,self.x)
            self.data_line_1.setData(self.t,self.x2)
            self.data_line_2.setData(self.t,self.x3)
            self.data_line_3.setData(self.t,self.x4)
            self.data_line_4.setData(self.t,self.x5)
            self.data_line_5.setData(self.t,self.x6)
            self.data_line_6.setData(self.t,self.x7)
            self.data_line_7.setData(self.t,self.x8)
            self.data_line_8.setData(self.t,self.x9)
           
        else:
            if not self.firstRun1:
                self.t = list(self.t)
                self.firstRun1.append(1)
                self.t = self.t[1:]
                self.t.append(self.t[-1]+1)
                self.xi,self.yi,self.zi = adxl.adxlfor()
                
                self.x =  self.x[1:]
                self.x2 = self.x2[1:]
                self.x3 = self.x3[1:]
                self.x4 = self.x4[1:]
                self.x5 = self.x5[1:]
                self.x6 = self.x6[1:]
                self.x7 = self.x7[1:]
                self.x8 = self.x8[1:]
                self.x9 = self.x9[1:]
               
                self.x.append(self.xi)
                self.x2.append(self.xi)
                self.x3.append(self.xi)
                self.x4.append(self.xi)
                self.x5.append(self.xi)
                self.x6.append(self.xi)
                self.x7.append(self.xi)
                self.x8.append(self.xi)
                self.x9.append(self.xi)
                
                self.data_line.setData(self.t,self.x)
                self.data_line_1.setData(self.t,self.x2)
                self.data_line_2.setData(self.t,self.x3)
                self.data_line_3.setData(self.t,self.x4)
                self.data_line_4.setData(self.t,self.x5)
                self.data_line_5.setData(self.t,self.x6)
                self.data_line_6.setData(self.t,self.x7)
                self.data_line_7.setData(self.t,self.x8)
                self.data_line_8.setData(self.t,self.x9)
                
            self.t = self.t[1:]
            self.t.append(self.t[-1]+1)
            self.xi,self.yi,self.zi = adxl.adxlfor()
            self.x =  self.x[1:]
            self.x2 = self.x2[1:]
            self.x3 = self.x3[1:]
            self.x4 = self.x4[1:]
            self.x5 = self.x5[1:]
            self.x6 = self.x6[1:]
            self.x7 = self.x7[1:]
            self.x8 = self.x8[1:]
            self.x9 = self.x9[1:]
            self.x.append(self.xi)
            self.x2.append(self.xi)
            self.x3.append(self.xi)
            self.x4.append(self.xi)
            self.x5.append(self.xi)
            self.x6.append(self.xi)
            self.x7.append(self.xi)
            self.x8.append(self.xi)
            self.x9.append(self.xi)
            
            self.data_line.setData(self.t,self.x)
            self.data_line_1.setData(self.t,self.x2)
            self.data_line_2.setData(self.t,self.x3)
            self.data_line_3.setData(self.t,self.x4)
            self.data_line_4.setData(self.t,self.x5)
            self.data_line_5.setData(self.t,self.x6)
            self.data_line_6.setData(self.t,self.x7)
            self.data_line_7.setData(self.t,self.x8)
            self.data_line_8.setData(self.t,self.x9)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

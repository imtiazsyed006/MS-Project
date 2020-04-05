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

class MyMplCanvas(FigureCanvas):

    def __init__(self, parent = None, dpi = 100):
        fig = plt.figure(tight_layout = True, dpi = 100)
        self.axes = fig.add_subplot(111)
        
        self.compute_initial_figure()
        FigureCanvas. __init__(self, fig)
        self.setParent(parent)

    def compute_initial_figure(self):
        pass

class Plot_1(MyMplCanvas):

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
        a,b,c = adxl345.Get_ADXL345_Values()
        
        a = int(a)
        b = int(b)
        c = int(c)
        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()
            
class Plot_2(MyMplCanvas):


    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()
        
class Plot_3(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

class Plot_4(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

class Plot_5(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

            
class Plot_6(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

            
class Plot_7(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

            
class Plot_8(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()

            
class Plot_9(MyMplCanvas):
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start()

    def compute_initial_figure(self):
        self.axes.plot()

    def update_figure(self):
        
##        a,b,c = adxl345.Get_ADXL345_Values()
##        
##        a = int(a)
##        b = int(b)
##        c = int(c)
##        angleFaccel.append(a)
        t = np.arange(0,len(angleFaccel))
        if len(angleFaccel) < 40:
            
            k = t
            self.axes.cla()
            self.axes.plot(k,angleFaccel,'r')
            self.axes.set_xlabel('time')
            self.draw()
        
        else:
            k = t[-39:]
            anew = angleFaccel[-39:]
            self.axes.cla()
            self.axes.plot(k,anew,'r')
            self.draw()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 256, 144))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setAcceptDrops(False)
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 144, 256, 144))
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 288, 256, 144))
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 432, 256, 144))
        self.widget_4.setObjectName("widget_4")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 576, 256, 144))
        self.widget_5.setObjectName("widget_5")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(256, 0, 256, 144))
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(512, 0, 256, 144))
        self.widget_7.setObjectName("widget_7")
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(768, 0, 256, 144))
        self.widget_8.setObjectName("widget_8")
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
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
        self.widget_10.setStyleSheet("border-color: rgb(255, 11, 210);\n"
"background-color: rgb(0, 0, 0);")
        self.widget_10.setObjectName("widget_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        a_1 = QtWidgets.QHBoxLayout(self.widget)
        b_1 = Plot_1(self.widget, dpi = 100)
        a_1.addWidget(b_1)

        a_2 = QtWidgets.QHBoxLayout(self.widget_2)
        b_2 = Plot_2(self.widget_2, dpi = 100)
        a_2.addWidget(b_2)

        a_3 = QtWidgets.QHBoxLayout(self.widget_3)
        b_3 = Plot_3(self.widget_3, dpi = 100)
        a_3.addWidget(b_3)

        a_4 = QtWidgets.QHBoxLayout(self.widget_4)
        b_4 = Plot_4(self.widget_4, dpi = 100)
        a_4.addWidget(b_4)

        a_5 = QtWidgets.QHBoxLayout(self.widget_5)
        b_5 = Plot_5(self.widget_5, dpi = 100)
        a_5.addWidget(b_5)

        a_6 = QtWidgets.QHBoxLayout(self.widget_6)
        b_6 = Plot_6(self.widget_6, dpi = 100)
        a_6.addWidget(b_6)

        a_7 = QtWidgets.QHBoxLayout(self.widget_7)
        b_7 = Plot_7(self.widget_7, dpi = 100)
        a_7.addWidget(b_7)

        a_8 = QtWidgets.QHBoxLayout(self.widget_8)
        b_8 = Plot_8(self.widget_8, dpi = 100)
        a_8.addWidget(b_8)

        a_9 = QtWidgets.QHBoxLayout(self.widget_9)
        b_9 = Plot_9(self.widget_9, dpi = 100)
        a_9.addWidget(b_9)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Raw Telemetry Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

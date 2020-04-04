from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import matplotlib.pyplot as plt
import ADXL345 as adxl345
from drawnow import*
import numpy as np
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
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [np.random.randint(0, 10) for i in range(4)]
        a,b,c = adxl345.Get_ADXL345_Values()
        
        a = int(a)
        b = int(b)
        c = int(c)
        
        angleFaccel.append(a)
        self.axes.cla()
        self.axes.plot(angleFaccel,'r')
        self.axes.set_xlabel('time')
        self.draw()
    


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 760)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 110, 40))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 0, 110, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(920, 0, 400, 150))
        self.widget.setObjectName("widget")
        
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(920, 190, 400, 150))
        self.widget_2.setObjectName("widget_2")
        
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(920, 340, 401, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(920, 380, 400, 150))
        self.widget_3.setObjectName("widget_3")
        
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(920, 530, 401, 41))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(920, 150, 401, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(1230, 570, 91, 121))
        self.dial.setObjectName("dial")
        
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(1070, 570, 91, 121))
        self.dial_2.setObjectName("dial_2")
        
        self.dial_3 = QtWidgets.QDial(self.centralwidget)
        self.dial_3.setGeometry(QtCore.QRect(920, 570, 91, 121))
        self.dial_3.setObjectName("dial_3")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(920, 680, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1070, 680, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1230, 680, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(930, 700, 71, 31))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(1080, 700, 71, 31))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(1240, 700, 71, 31))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 280, 500, 170))
        self.widget_4.setObjectName("widget_4")
        
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(0, 70, 500, 170))
        self.widget_5.setObjectName("widget_5")
        
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(0, 490, 500, 170))
        self.widget_6.setObjectName("widget_6")
        
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(0, 660, 501, 41))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(0, 450, 501, 41))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(0, 240, 501, 41))
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        l = QtWidgets.QHBoxLayout(self.widget)
        sc = Plot_1(self.widget, dpi = 100)
        l.addWidget(sc)
        

    
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remotely Operated Vehicle Dashboard"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "  Roll"))
        self.label_2.setText(_translate("MainWindow", "   Pitch"))
        self.label_3.setText(_translate("MainWindow", " Yaw"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



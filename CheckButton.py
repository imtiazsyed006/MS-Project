
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 40, 161, 101))
        self.checkBox.stateChanged.connect(self.logData)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(24, 24))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.fileName = ''
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.dataLog)
        self.timer.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))

    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')

    def dataLog(self):
        if not self.fileName:
            pass
        else:
            with open(self.fileName + '.txt','a') as file:
                file.write(str(1)+'\n')

    def logData(self,state):
        
        if state == QtCore.Qt.Checked:
            year   = time.localtime().tm_year
            month  = time.localtime().tm_mon
            day    = time.localtime().tm_mday
            hour   = time.localtime().tm_hour
            minute = time.localtime().tm_min
            second = time.localtime().tm_sec

            self.fileName = str(year)+'_'+str(month)+'_'+str(day)+'_'+str(hour)+'_'+str(minute)+'_'+str(second)
            # with open(fileName + str('.txt'),'a') as file:
            #     file.write(str(1)+'\n')

        else:
            self.fileName = ''
            print('Data logging stopped')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

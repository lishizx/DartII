# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\MainDant.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDant(object):
    def setupUi(self, MainDant):
        MainDant.setObjectName("MainDant")
        MainDant.resize(1200, 600)
        MainDant.setMinimumSize(QtCore.QSize(1200, 600))
        MainDant.setMaximumSize(QtCore.QSize(1200, 600))
        MainDant.setSizeIncrement(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDant.setWindowIcon(icon)
        MainDant.setStyleSheet("background-color:#FFFFFF;")
        self.centralwidget = QtWidgets.QWidget(MainDant)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, -10, 1201, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.MaingridLayout.setContentsMargins(0, 9, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.USERROOT = QtWidgets.QLabel(self.centralwidget)
        self.USERROOT.setGeometry(QtCore.QRect(0, 650, 54, 12))
        self.USERROOT.setObjectName("USERROOT")
        MainDant.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainDant)
        QtCore.QMetaObject.connectSlotsByName(MainDant)

    def retranslateUi(self, MainDant):
        _translate = QtCore.QCoreApplication.translate
        MainDant.setWindowTitle(_translate("MainDant", "MainWindow"))
        self.USERROOT.setText(_translate("MainDant", "0"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDant = QtWidgets.QMainWindow()
    ui = Ui_MainDant()
    ui.setupUi(MainDant)
    MainDant.show()
    sys.exit(app.exec_())


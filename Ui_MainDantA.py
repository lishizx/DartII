# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\MainDantA.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDantA(object):
    def setupUi(self, MainDantA):
        MainDantA.setObjectName("MainDantA")
        MainDantA.resize(1200, 600)
        MainDantA.setMinimumSize(QtCore.QSize(1200, 600))
        MainDantA.setMaximumSize(QtCore.QSize(1200, 600))
        MainDantA.setSizeIncrement(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainDantA.setWindowIcon(icon)
        MainDantA.setStyleSheet("background-color:#FFFFFF;")
        self.centralwidget = QtWidgets.QWidget(MainDantA)
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
        MainDantA.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainDantA)
        QtCore.QMetaObject.connectSlotsByName(MainDantA)

    def retranslateUi(self, MainDantA):
        _translate = QtCore.QCoreApplication.translate
        MainDantA.setWindowTitle(_translate("MainDantA", "MainWindow"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDantA = QtWidgets.QMainWindow()
    ui = Ui_MainDantA()
    ui.setupUi(MainDantA)
    MainDantA.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\Minaco.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
class Ui_Minaco(object):
    def setupUi(self, Minaco):
        self.setWindowFlags(Qt.FramelessWindowHint)
        Minaco.setObjectName("Minaco")
        Minaco.setWindowModality(QtCore.Qt.NonModal)
        Minaco.setEnabled(True)
        Minaco.resize(1200, 600)
        Minaco.setMinimumSize(QtCore.QSize(1200, 600))
        Minaco.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Minaco.setWindowIcon(icon)
        Minaco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backimg = QtWidgets.QLabel(Minaco)
        self.backimg.setGeometry(QtCore.QRect(0, 0, 1201, 601))
        self.backimg.setText("")
        self.backimg.setPixmap(QtGui.QPixmap(":/image/welcome.jpg"))
        self.backimg.setScaledContents(True)
        self.backimg.setObjectName("backimg")
        self.loadtext = QtWidgets.QLabel(Minaco)
        self.loadtext.setGeometry(QtCore.QRect(1010, 560, 141, 20))
        self.loadtext.setStyleSheet("background:none;\n"
"color:#FFFFFF;")
        self.loadtext.setObjectName("loadtext")
        self.loadgif = QtWidgets.QLabel(Minaco)
        self.loadgif.setGeometry(QtCore.QRect(990, 562, 16, 16))
        self.loadgif.setStyleSheet("background:none;")
        self.loadgif.setText("")
        self.loadgif.setPixmap(QtGui.QPixmap(":/image/loading.gif"))
        self.loadgif.setScaledContents(True)
        self.loadgif.setObjectName("loadgif")
        self.movie =  QMovie(":/image/loading.gif")
        self.loadgif.setMovie(self.movie)
        self.movie.start()
        self.retranslateUi(Minaco)
        QtCore.QMetaObject.connectSlotsByName(Minaco)

    def retranslateUi(self, Minaco):
        _translate = QtCore.QCoreApplication.translate
        Minaco.setWindowTitle(_translate("Minaco", "扫描工具v2"))
        self.loadtext.setText(_translate("Minaco", "正在加载资源配置..."))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Minaco = QtWidgets.QWidget()
    ui = Ui_Minaco()
    ui.setupUi(Minaco)
    Minaco.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.NonModal)
        Login.setEnabled(True)
        Login.resize(1200, 600)
        Login.setMinimumSize(QtCore.QSize(1200, 600))
        Login.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backimg = QtWidgets.QLabel(Login)
        self.backimg.setGeometry(QtCore.QRect(0, 0, 1201, 601))
        self.backimg.setText("")
        self.backimg.setPixmap(QtGui.QPixmap(":/image/welcome.jpg"))
        self.backimg.setScaledContents(True)
        self.backimg.setObjectName("backimg")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(910, 220, 241, 271))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-radius:5px;")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(Login)
        self.username.setGeometry(QtCore.QRect(936, 300, 191, 31))
        self.username.setStyleSheet("padding-left:5px;")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(936, 257, 3, 20))
        self.label_2.setStyleSheet("width:4px;\n"
"height:10px;\n"
"background:#188EEE;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(945, 260, 91, 16))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(Login)
        self.password.setGeometry(QtCore.QRect(936, 350, 191, 31))
        self.password.setStyleSheet("padding-left:5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(Login)
        self.loginbtn.setGeometry(QtCore.QRect(936, 430, 191, 31))
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"border-radius:3px;")
        self.loginbtn.setObjectName("loginbtn")
        self.tip = QtWidgets.QLabel(Login)
        self.tip.setGeometry(QtCore.QRect(1043, 400, 91, 16))
        self.tip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tip.setStyleSheet("color:red;\n"
"text-align:center;")
        self.tip.setText("")
        self.tip.setObjectName("tip")
        self.inadmin = QtWidgets.QPushButton(Login)
        self.inadmin.setGeometry(QtCore.QRect(930, 390, 71, 31))
        self.inadmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inadmin.setStyleSheet("border:none;\n"
"background:none;\n"
"color:red;\n"
"border-radius:3px;")
        self.inadmin.setObjectName("inadmin")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "扫描工具v2"))
        self.username.setPlaceholderText(_translate("Login", "请输入用户名"))
        self.label_3.setText(_translate("Login", "用户登录"))
        self.password.setPlaceholderText(_translate("Login", "请输入密码"))
        self.loginbtn.setText(_translate("Login", "登 录"))
        self.inadmin.setText(_translate("Login", "管理员界面"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


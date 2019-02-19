# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\Admin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.setWindowModality(QtCore.Qt.ApplicationModal)
        Admin.setEnabled(True)
        Admin.resize(1200, 600)
        Admin.setMinimumSize(QtCore.QSize(1200, 600))
        Admin.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Admin.setWindowIcon(icon)
        Admin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backimg = QtWidgets.QLabel(Admin)
        self.backimg.setGeometry(QtCore.QRect(0, 0, 1201, 601))
        self.backimg.setText("")
        self.backimg.setPixmap(QtGui.QPixmap(":/image/welcome.jpg"))
        self.backimg.setScaledContents(True)
        self.backimg.setObjectName("backimg")
        self.label = QtWidgets.QLabel(Admin)
        self.label.setGeometry(QtCore.QRect(910, 220, 241, 271))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-radius:5px;")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(Admin)
        self.username.setGeometry(QtCore.QRect(936, 300, 191, 31))
        self.username.setStyleSheet("padding-left:5px;")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(Admin)
        self.label_2.setGeometry(QtCore.QRect(936, 257, 3, 20))
        self.label_2.setStyleSheet("width:4px;\n"
"height:10px;\n"
"background:#188EEE;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Admin)
        self.label_3.setGeometry(QtCore.QRect(945, 260, 91, 16))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(Admin)
        self.password.setGeometry(QtCore.QRect(936, 350, 191, 31))
        self.password.setStyleSheet("padding-left:5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(Admin)
        self.loginbtn.setGeometry(QtCore.QRect(936, 430, 191, 31))
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"border-radius:3px;")
        self.loginbtn.setObjectName("loginbtn")
        self.gouser = QtWidgets.QPushButton(Admin)
        self.gouser.setGeometry(QtCore.QRect(924, 392, 75, 23))
        self.gouser.setStyleSheet("border:none;\n"
"color:red;")
        self.gouser.setObjectName("gouser")
        self.tip = QtWidgets.QLabel(Admin)
        self.tip.setGeometry(QtCore.QRect(1040, 398, 91, 16))
        self.tip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tip.setStyleSheet("color:red;\n"
"text-align:center;")
        self.tip.setText("")
        self.tip.setObjectName("tip")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "扫描工具v2"))
        self.username.setPlaceholderText(_translate("Admin", "请输入用户名"))
        self.label_3.setText(_translate("Admin", "管理员登录"))
        self.password.setPlaceholderText(_translate("Admin", "请输入密码"))
        self.loginbtn.setText(_translate("Admin", "登 录"))
        self.gouser.setText(_translate("Admin", "用户界面"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())


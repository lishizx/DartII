# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\EditUser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditUser(object):
    def setupUi(self, EditUser):
        EditUser.setObjectName("EditUser")
        EditUser.resize(289, 403)
        EditUser.setMinimumSize(QtCore.QSize(0, 320))
        EditUser.setMaximumSize(QtCore.QSize(16777215, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        EditUser.setWindowIcon(icon)
        EditUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.username = QtWidgets.QLineEdit(EditUser)
        self.username.setGeometry(QtCore.QRect(30, 71, 231, 31))
        self.username.setStyleSheet("padding-left:5px;")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setReadOnly(True)
        self.username.setObjectName("username")
        self.update = QtWidgets.QPushButton(EditUser)
        self.update.setGeometry(QtCore.QRect(30, 340, 231, 31))
        self.update.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"border-radius:3px;")
        self.update.setObjectName("update")
        self.password = QtWidgets.QLineEdit(EditUser)
        self.password.setGeometry(QtCore.QRect(30, 170, 231, 31))
        self.password.setStyleSheet("padding-left:5px;")
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.nickname = QtWidgets.QLineEdit(EditUser)
        self.nickname.setGeometry(QtCore.QRect(30, 120, 231, 31))
        self.nickname.setStyleSheet("padding-left:5px;")
        self.nickname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nickname.setObjectName("nickname")
        self.label_3 = QtWidgets.QLabel(EditUser)
        self.label_3.setGeometry(QtCore.QRect(39, 32, 91, 16))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setObjectName("label_3")
        self.password2 = QtWidgets.QLineEdit(EditUser)
        self.password2.setGeometry(QtCore.QRect(30, 220, 231, 31))
        self.password2.setStyleSheet("padding-left:5px;")
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setObjectName("password2")
        self.label_2 = QtWidgets.QLabel(EditUser)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 3, 20))
        self.label_2.setStyleSheet("width:4px;\n"
"height:10px;\n"
"background:#188EEE;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.root = QtWidgets.QComboBox(EditUser)
        self.root.setGeometry(QtCore.QRect(30, 280, 191, 30))
        self.root.setObjectName("root")
        self.root.addItem("")
        self.root.addItem("")
        self.root.addItem("")
        self.root.addItem("")
        self.label_4 = QtWidgets.QLabel(EditUser)
        self.label_4.setGeometry(QtCore.QRect(230, 283, 31, 20))
        self.label_4.setStyleSheet("font-size:16px;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(EditUser)
        QtCore.QMetaObject.connectSlotsByName(EditUser)

    def retranslateUi(self, EditUser):
        _translate = QtCore.QCoreApplication.translate
        EditUser.setWindowTitle(_translate("EditUser", "编辑用户"))
        self.username.setPlaceholderText(_translate("EditUser", "用户名"))
        self.update.setText(_translate("EditUser", "保 存"))
        self.password.setPlaceholderText(_translate("EditUser", "请输入密码"))
        self.nickname.setPlaceholderText(_translate("EditUser", "用户昵称"))
        self.label_3.setText(_translate("EditUser", "编辑用户"))
        self.password2.setPlaceholderText(_translate("EditUser", "请重复输入密码"))
        self.root.setItemText(0, _translate("EditUser", "超级管理员"))
        self.root.setItemText(1, _translate("EditUser", "打印条码"))
        self.root.setItemText(2, _translate("EditUser", "出库扫描"))
        self.root.setItemText(3, _translate("EditUser", "两个都可以"))
        self.label_4.setText(_translate("EditUser", "权限"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditUser = QtWidgets.QWidget()
    ui = Ui_EditUser()
    ui.setupUi(EditUser)
    EditUser.show()
    sys.exit(app.exec_())


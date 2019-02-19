# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\Dataset.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dataset(object):
    def setupUi(self, Dataset):
        Dataset.setObjectName("Dataset")
        Dataset.setWindowModality(QtCore.Qt.NonModal)
        Dataset.setEnabled(True)
        Dataset.resize(900, 500)
        Dataset.setMinimumSize(QtCore.QSize(900, 500))
        Dataset.setMaximumSize(QtCore.QSize(900, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dataset.setWindowIcon(icon)
        Dataset.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.backimg = QtWidgets.QLabel(Dataset)
        self.backimg.setGeometry(QtCore.QRect(0, 0, 1201, 601))
        self.backimg.setText("")
        self.backimg.setPixmap(QtGui.QPixmap(":/image/hostback.jpg"))
        self.backimg.setScaledContents(True)
        self.backimg.setObjectName("backimg")
        self.label = QtWidgets.QLabel(Dataset)
        self.label.setGeometry(QtCore.QRect(324, 96, 281, 311))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-radius:5px;")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(Dataset)
        self.username.setGeometry(QtCore.QRect(350, 253, 231, 31))
        self.username.setStyleSheet("padding-left:5px;")
        self.username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(Dataset)
        self.label_2.setGeometry(QtCore.QRect(350, 128, 3, 20))
        self.label_2.setStyleSheet("width:4px;\n"
"height:10px;\n"
"background:#188EEE;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dataset)
        self.label_3.setGeometry(QtCore.QRect(359, 130, 91, 16))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(Dataset)
        self.password.setGeometry(QtCore.QRect(350, 295, 231, 31))
        self.password.setStyleSheet("padding-left:5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbtn = QtWidgets.QPushButton(Dataset)
        self.loginbtn.setGeometry(QtCore.QRect(350, 352, 231, 31))
        self.loginbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbtn.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"border-radius:3px;")
        self.loginbtn.setObjectName("loginbtn")
        self.host = QtWidgets.QLineEdit(Dataset)
        self.host.setGeometry(QtCore.QRect(350, 166, 231, 31))
        self.host.setStyleSheet("padding-left:5px;")
        self.host.setInputMethodHints(QtCore.Qt.ImhNone)
        self.host.setObjectName("host")
        self.dataname = QtWidgets.QLineEdit(Dataset)
        self.dataname.setGeometry(QtCore.QRect(350, 210, 231, 31))
        self.dataname.setStyleSheet("padding-left:5px;")
        self.dataname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dataname.setObjectName("dataname")
        self.tip = QtWidgets.QLabel(Dataset)
        self.tip.setGeometry(QtCore.QRect(350, 330, 101, 16))
        self.tip.setStyleSheet("color:#41CD52")
        self.tip.setText("")
        self.tip.setObjectName("tip")

        self.retranslateUi(Dataset)
        QtCore.QMetaObject.connectSlotsByName(Dataset)

    def retranslateUi(self, Dataset):
        _translate = QtCore.QCoreApplication.translate
        Dataset.setWindowTitle(_translate("Dataset", "扫描工具v2"))
        self.username.setPlaceholderText(_translate("Dataset", "请输入用户名"))
        self.label_3.setText(_translate("Dataset", "数据库配置"))
        self.password.setPlaceholderText(_translate("Dataset", "请输入密码"))
        self.loginbtn.setText(_translate("Dataset", "保 存"))
        self.host.setPlaceholderText(_translate("Dataset", "请输入IP地址"))
        self.dataname.setPlaceholderText(_translate("Dataset", "请输入数据库名"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dataset = QtWidgets.QWidget()
    ui = Ui_Dataset()
    ui.setupUi(Dataset)
    Dataset.show()
    sys.exit(app.exec_())


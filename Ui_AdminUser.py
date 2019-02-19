# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\AdminUser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminUser(object):
    def setupUi(self, AdminUser):
        AdminUser.setObjectName("AdminUser")
        AdminUser.setWindowModality(QtCore.Qt.NonModal)
        AdminUser.setEnabled(True)
        AdminUser.resize(1200, 600)
        AdminUser.setMinimumSize(QtCore.QSize(1200, 600))
        AdminUser.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        AdminUser.setWindowIcon(icon)
        AdminUser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(AdminUser)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 70))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background:#000;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tab2 = QtWidgets.QPushButton(AdminUser)
        self.tab2.setGeometry(QtCore.QRect(90, 0, 90, 70))
        self.tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab2.setStyleSheet("border:none;\n"
"background:#000;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab2.setText("")
        self.tab2.setObjectName("tab2")
        self.gosearch = QtWidgets.QPushButton(AdminUser)
        self.gosearch.setGeometry(QtCore.QRect(1090, 80, 91, 41))
        self.gosearch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gosearch.setStyleSheet("border:none;\n"
"background:#222;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.gosearch.setObjectName("gosearch")
        self.tab3 = QtWidgets.QPushButton(AdminUser)
        self.tab3.setGeometry(QtCore.QRect(180, 0, 90, 70))
        self.tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab3.setStyleSheet("border:none;\n"
"background:#000;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab3.setText("")
        self.tab3.setObjectName("tab3")
        self.tab4 = QtWidgets.QPushButton(AdminUser)
        self.tab4.setGeometry(QtCore.QRect(270, 0, 90, 70))
        self.tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab4.setStyleSheet("border:none;\n"
"background:#000;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab4.setText("")
        self.tab4.setObjectName("tab4")
        self.tab1 = QtWidgets.QPushButton(AdminUser)
        self.tab1.setGeometry(QtCore.QRect(0, 0, 90, 70))
        self.tab1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab1.setStyleSheet("border:none;\n"
"background:#222;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab1.setObjectName("tab1")
        self.search = QtWidgets.QLineEdit(AdminUser)
        self.search.setGeometry(QtCore.QRect(110, 80, 971, 40))
        self.search.setStyleSheet("padding-left:10px;\n"
"font-size:16px;\n"
"font: 75 18pt \"AngsanaUPC\";")
        self.search.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.search.setObjectName("search")
        self.add = QtWidgets.QPushButton(AdminUser)
        self.add.setGeometry(QtCore.QRect(20, 80, 81, 41))
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setStyleSheet("border:none;\n"
"background:#222;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.add.setObjectName("add")
        self.exits = QtWidgets.QPushButton(AdminUser)
        self.exits.setGeometry(QtCore.QRect(1146, 15, 40, 40))
        self.exits.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exits.setStyleSheet("border:none;\n"
"background:#000;\n"
"color:#FFFFFF;")
        self.exits.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exits.setIcon(icon1)
        self.exits.setIconSize(QtCore.QSize(30, 30))
        self.exits.setObjectName("exits")
        self.codelist = QtWidgets.QTableWidget(AdminUser)
        self.codelist.setGeometry(QtCore.QRect(20, 130, 1161, 451))
        self.codelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codelist.setObjectName("codelist")
        self.codelist.setColumnCount(0)
        self.codelist.setRowCount(0)
        self.shuaxin = QtWidgets.QPushButton(AdminUser)
        self.shuaxin.setGeometry(QtCore.QRect(1100, 15, 40, 40))
        self.shuaxin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shuaxin.setStyleSheet("border:none;\n"
"background:#000;\n"
"color:#FFFFFF;")
        self.shuaxin.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/shuaxin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuaxin.setIcon(icon2)
        self.shuaxin.setIconSize(QtCore.QSize(30, 30))
        self.shuaxin.setObjectName("shuaxin")

        self.retranslateUi(AdminUser)
        QtCore.QMetaObject.connectSlotsByName(AdminUser)

    def retranslateUi(self, AdminUser):
        _translate = QtCore.QCoreApplication.translate
        AdminUser.setWindowTitle(_translate("AdminUser", "扫描工具v2"))
        self.gosearch.setText(_translate("AdminUser", "查找"))
        self.tab1.setText(_translate("AdminUser", "用户列表"))
        self.search.setPlaceholderText(_translate("AdminUser", "请输入您要搜索的用户昵称"))
        self.add.setText(_translate("AdminUser", "添加"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminUser = QtWidgets.QWidget()
    ui = Ui_AdminUser()
    ui.setupUi(AdminUser)
    AdminUser.show()
    sys.exit(app.exec_())


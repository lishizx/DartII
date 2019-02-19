# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\OutCode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OutCode(object):
    def setupUi(self, OutCode):
        OutCode.setObjectName("OutCode")
        OutCode.setWindowModality(QtCore.Qt.ApplicationModal)
        OutCode.setEnabled(True)
        OutCode.resize(1200, 600)
        OutCode.setMinimumSize(QtCore.QSize(1200, 600))
        OutCode.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        OutCode.setWindowIcon(icon)
        OutCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(OutCode)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 70))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background:#188eee;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(OutCode)
        self.pushButton_2.setGeometry(QtCore.QRect(1090, 540, 81, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFF;\n"
"font-size:14px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.code = QtWidgets.QLineEdit(OutCode)
        self.code.setGeometry(QtCore.QRect(30, 540, 1041, 40))
        self.code.setStyleSheet("padding-left:10px;\n"
"font-size:16px;\n"
"font: 75 18pt \"AngsanaUPC\";")
        self.code.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.code.setObjectName("code")
        self.outcode = QtWidgets.QLineEdit(OutCode)
        self.outcode.setGeometry(QtCore.QRect(30, 490, 1041, 40))
        self.outcode.setStyleSheet("padding-left:10px;\n"
"font-size:16px;\n"
"font: 75 18pt \"AngsanaUPC\";")
        self.outcode.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.outcode.setObjectName("outcode")
        self.pack = QtWidgets.QPushButton(OutCode)
        self.pack.setGeometry(QtCore.QRect(1090, 490, 81, 41))
        self.pack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pack.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFF;\n"
"font-size:14px;")
        self.pack.setObjectName("pack")
        self.shuaxin = QtWidgets.QPushButton(OutCode)
        self.shuaxin.setGeometry(QtCore.QRect(1130, 15, 40, 40))
        self.shuaxin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shuaxin.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;")
        self.shuaxin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/shuaxin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuaxin.setIcon(icon1)
        self.shuaxin.setIconSize(QtCore.QSize(30, 30))
        self.shuaxin.setObjectName("shuaxin")
        self.codelist = QtWidgets.QTableWidget(OutCode)
        self.codelist.setGeometry(QtCore.QRect(30, 90, 1141, 381))
        self.codelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codelist.setObjectName("codelist")
        self.codelist.setColumnCount(0)
        self.codelist.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(OutCode)
        self.label_2.setGeometry(QtCore.QRect(910, 20, 131, 31))
        self.label_2.setStyleSheet("font-size:20px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.label_2.setObjectName("label_2")
        self.count = QtWidgets.QLabel(OutCode)
        self.count.setGeometry(QtCore.QRect(1040, 20, 81, 31))
        self.count.setStyleSheet("font-size:20px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.count.setObjectName("count")
        self.yushe = QtWidgets.QLabel(OutCode)
        self.yushe.setGeometry(QtCore.QRect(170, 5, 81, 31))
        self.yushe.setStyleSheet("font-size:16px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.yushe.setObjectName("yushe")
        self.label_3 = QtWidgets.QLabel(OutCode)
        self.label_3.setGeometry(QtCore.QRect(30, 4, 141, 31))
        self.label_3.setStyleSheet("font-size:16px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(OutCode)
        self.label_4.setGeometry(QtCore.QRect(47, 32, 121, 31))
        self.label_4.setStyleSheet("font-size:16px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.label_4.setObjectName("label_4")
        self.nownum = QtWidgets.QLabel(OutCode)
        self.nownum.setGeometry(QtCore.QRect(170, 32, 81, 31))
        self.nownum.setStyleSheet("font-size:16px;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-weight:bold;")
        self.nownum.setObjectName("nownum")
        self.tab1 = QtWidgets.QPushButton(OutCode)
        self.tab1.setGeometry(QtCore.QRect(300, 0, 140, 70))
        self.tab1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab1.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab1.setObjectName("tab1")
        self.tab2 = QtWidgets.QPushButton(OutCode)
        self.tab2.setGeometry(QtCore.QRect(440, 0, 140, 70))
        self.tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab2.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab2.setObjectName("tab2")
        self.tab4 = QtWidgets.QPushButton(OutCode)
        self.tab4.setGeometry(QtCore.QRect(670, 0, 131, 70))
        self.tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab4.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab4.setObjectName("tab4")
        self.tab3 = QtWidgets.QPushButton(OutCode)
        self.tab3.setGeometry(QtCore.QRect(580, 0, 90, 70))
        self.tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab3.setStyleSheet("border:none;\n"
"background:#349BFF;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab3.setObjectName("tab3")
        self.tab5 = QtWidgets.QPushButton(OutCode)
        self.tab5.setGeometry(QtCore.QRect(800, 0, 90, 70))
        self.tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab5.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab5.setObjectName("tab5")

        self.retranslateUi(OutCode)
        QtCore.QMetaObject.connectSlotsByName(OutCode)

    def retranslateUi(self, OutCode):
        _translate = QtCore.QCoreApplication.translate
        OutCode.setWindowTitle(_translate("OutCode", "扫描工具v2"))
        self.pushButton_2.setText(_translate("OutCode", "刷新"))
        self.code.setPlaceholderText(_translate("OutCode", "请输入出库条码"))
        self.outcode.setPlaceholderText(_translate("OutCode", "请输入外箱条码"))
        self.pack.setText(_translate("OutCode", "手动打包"))
        self.label_2.setText(_translate("OutCode", "今日扫描数量"))
        self.count.setText(_translate("OutCode", "0"))
        self.yushe.setText(_translate("OutCode", "0"))
        self.label_3.setText(_translate("OutCode", "外箱条码预设数量"))
        self.label_4.setText(_translate("OutCode", "已使用打包数量"))
        self.nownum.setText(_translate("OutCode", "0"))
        self.tab1.setText(_translate("OutCode", "产品条码管理"))
        self.tab2.setText(_translate("OutCode", "外箱条码管理"))
        self.tab4.setText(_translate("OutCode", "打印出货标签"))
        self.tab3.setText(_translate("OutCode", "出库扫描"))
        self.tab5.setText(_translate("OutCode", "出货扫描"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutCode = QtWidgets.QWidget()
    ui = Ui_OutCode()
    ui.setupUi(OutCode)
    OutCode.show()
    sys.exit(app.exec_())


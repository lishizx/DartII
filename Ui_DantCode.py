# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\DantCode.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DantCode(object):
    def setupUi(self, DantCode):
        DantCode.setObjectName("DantCode")
        DantCode.setWindowModality(QtCore.Qt.ApplicationModal)
        DantCode.setEnabled(True)
        DantCode.resize(1200, 600)
        DantCode.setMinimumSize(QtCore.QSize(1200, 600))
        DantCode.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DantCode.setWindowIcon(icon)
        DantCode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(DantCode)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 70))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background:#188eee;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.bulkprint = QtWidgets.QPushButton(DantCode)
        self.bulkprint.setGeometry(QtCore.QRect(1100, 540, 81, 41))
        self.bulkprint.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bulkprint.setStyleSheet("border:none;\n"
"background:#FFCD43;\n"
"color:#FFF;\n"
"font-size:14px;")
        self.bulkprint.setObjectName("bulkprint")
        self.codeset = QtWidgets.QPushButton(DantCode)
        self.codeset.setGeometry(QtCore.QRect(1140, 15, 40, 40))
        self.codeset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.codeset.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;")
        self.codeset.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.codeset.setIcon(icon1)
        self.codeset.setIconSize(QtCore.QSize(30, 30))
        self.codeset.setObjectName("codeset")
        self.bulkdel = QtWidgets.QPushButton(DantCode)
        self.bulkdel.setGeometry(QtCore.QRect(90, 540, 80, 40))
        self.bulkdel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bulkdel.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;\n"
"font-size:14px;")
        self.bulkdel.setObjectName("bulkdel")
        self.creatcode = QtWidgets.QPushButton(DantCode)
        self.creatcode.setGeometry(QtCore.QRect(440, 540, 80, 40))
        self.creatcode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.creatcode.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;\n"
"font-size:14px;")
        self.creatcode.setObjectName("creatcode")
        self.creatnum = QtWidgets.QLineEdit(DantCode)
        self.creatnum.setGeometry(QtCore.QRect(370, 541, 61, 40))
        self.creatnum.setStyleSheet("padding-left:10px;\n"
"font-size:16px;")
        self.creatnum.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.creatnum.setObjectName("creatnum")
        self.selectAll = QtWidgets.QCheckBox(DantCode)
        self.selectAll.setGeometry(QtCore.QRect(30, 564, 51, 16))
        self.selectAll.setStyleSheet("font-size:16px;")
        self.selectAll.setObjectName("selectAll")
        self.comboBox = QtWidgets.QComboBox(DantCode)
        self.comboBox.setGeometry(QtCore.QRect(990, 540, 101, 41))
        self.comboBox.setObjectName("comboBox")
        self.choosurl = QtWidgets.QPushButton(DantCode)
        self.choosurl.setGeometry(QtCore.QRect(870, 540, 111, 40))
        self.choosurl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choosurl.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;\n"
"font-size:14px;")
        self.choosurl.setObjectName("choosurl")
        self.shuaxin = QtWidgets.QPushButton(DantCode)
        self.shuaxin.setGeometry(QtCore.QRect(1090, 15, 40, 40))
        self.shuaxin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shuaxin.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;")
        self.shuaxin.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/shuaxin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuaxin.setIcon(icon2)
        self.shuaxin.setIconSize(QtCore.QSize(30, 30))
        self.shuaxin.setObjectName("shuaxin")
        self.codelist = QtWidgets.QTableWidget(DantCode)
        self.codelist.setGeometry(QtCore.QRect(20, 90, 1161, 431))
        self.codelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codelist.setObjectName("codelist")
        self.codelist.setColumnCount(0)
        self.codelist.setRowCount(0)
        self.tab3 = QtWidgets.QPushButton(DantCode)
        self.tab3.setGeometry(QtCore.QRect(580, 0, 90, 70))
        self.tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab3.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab3.setObjectName("tab3")
        self.tab1 = QtWidgets.QPushButton(DantCode)
        self.tab1.setGeometry(QtCore.QRect(300, 0, 140, 70))
        self.tab1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab1.setStyleSheet("border:none;\n"
"background:#349BFF;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab1.setObjectName("tab1")
        self.tab4 = QtWidgets.QPushButton(DantCode)
        self.tab4.setGeometry(QtCore.QRect(670, 0, 131, 70))
        self.tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab4.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab4.setObjectName("tab4")
        self.tab5 = QtWidgets.QPushButton(DantCode)
        self.tab5.setGeometry(QtCore.QRect(800, 0, 90, 70))
        self.tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab5.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab5.setObjectName("tab5")
        self.tab2 = QtWidgets.QPushButton(DantCode)
        self.tab2.setGeometry(QtCore.QRect(440, 0, 140, 70))
        self.tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab2.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab2.setObjectName("tab2")
        self.label_2 = QtWidgets.QLabel(DantCode)
        self.label_2.setGeometry(QtCore.QRect(210, 545, 151, 31))
        self.label_2.setStyleSheet("font:20px;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DantCode)
        QtCore.QMetaObject.connectSlotsByName(DantCode)

    def retranslateUi(self, DantCode):
        _translate = QtCore.QCoreApplication.translate
        DantCode.setWindowTitle(_translate("DantCode", "扫描工具v2"))
        self.bulkprint.setText(_translate("DantCode", "批量打印"))
        self.bulkdel.setText(_translate("DantCode", "批量删除"))
        self.creatcode.setText(_translate("DantCode", "条码生成"))
        self.selectAll.setText(_translate("DantCode", "全选"))
        self.choosurl.setText(_translate("DantCode", "选择模板目录"))
        self.tab3.setText(_translate("DantCode", "出库扫描"))
        self.tab1.setText(_translate("DantCode", "产品条码管理"))
        self.tab4.setText(_translate("DantCode", "打印出货标签"))
        self.tab5.setText(_translate("DantCode", "出货扫描"))
        self.tab2.setText(_translate("DantCode", "外箱条码管理"))
        self.label_2.setText(_translate("DantCode", "请输入条码数量:"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DantCode = QtWidgets.QWidget()
    ui = Ui_DantCode()
    ui.setupUi(DantCode)
    DantCode.show()
    sys.exit(app.exec_())


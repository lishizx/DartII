# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\DantOutProt.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DantOutProt(object):
    def setupUi(self, DantOutProt):
        DantOutProt.setObjectName("DantOutProt")
        DantOutProt.setWindowModality(QtCore.Qt.ApplicationModal)
        DantOutProt.setEnabled(True)
        DantOutProt.resize(1200, 600)
        DantOutProt.setMinimumSize(QtCore.QSize(1200, 600))
        DantOutProt.setMaximumSize(QtCore.QSize(1200, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DantOutProt.setWindowIcon(icon)
        DantOutProt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(DantOutProt)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 70))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("background:#188eee;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.tab2 = QtWidgets.QPushButton(DantOutProt)
        self.tab2.setGeometry(QtCore.QRect(440, 0, 140, 70))
        self.tab2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab2.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab2.setObjectName("tab2")
        self.tab3 = QtWidgets.QPushButton(DantOutProt)
        self.tab3.setGeometry(QtCore.QRect(580, 0, 90, 70))
        self.tab3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab3.setStyleSheet("border:none;\n"
"background:#188eee;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab3.setObjectName("tab3")
        self.tab4 = QtWidgets.QPushButton(DantOutProt)
        self.tab4.setGeometry(QtCore.QRect(670, 0, 131, 70))
        self.tab4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab4.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab4.setObjectName("tab4")
        self.tab1 = QtWidgets.QPushButton(DantOutProt)
        self.tab1.setGeometry(QtCore.QRect(300, 0, 140, 70))
        self.tab1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab1.setStyleSheet("border:none;\n"
"background:#188EEE;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab1.setObjectName("tab1")
        self.shuaxin = QtWidgets.QPushButton(DantOutProt)
        self.shuaxin.setGeometry(QtCore.QRect(1140, 15, 40, 40))
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
        self.out = QtWidgets.QLineEdit(DantOutProt)
        self.out.setGeometry(QtCore.QRect(20, 550, 1161, 40))
        self.out.setStyleSheet("padding-left:10px;\n"
"font-size:16px;\n"
"font: 75 18pt \"AngsanaUPC\";")
        self.out.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.out.setObjectName("out")
        self.codelist = QtWidgets.QTableWidget(DantOutProt)
        self.codelist.setGeometry(QtCore.QRect(20, 90, 1161, 441))
        self.codelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codelist.setObjectName("codelist")
        self.codelist.setColumnCount(0)
        self.codelist.setRowCount(0)
        self.tab5 = QtWidgets.QPushButton(DantOutProt)
        self.tab5.setGeometry(QtCore.QRect(800, 0, 90, 70))
        self.tab5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab5.setStyleSheet("border:none;\n"
"background:#349BFF;\n"
"color:#FFFFFF;\n"
"font-size:16px;")
        self.tab5.setObjectName("tab5")

        self.retranslateUi(DantOutProt)
        QtCore.QMetaObject.connectSlotsByName(DantOutProt)

    def retranslateUi(self, DantOutProt):
        _translate = QtCore.QCoreApplication.translate
        DantOutProt.setWindowTitle(_translate("DantOutProt", "扫描工具v2"))
        self.tab2.setText(_translate("DantOutProt", "外箱条码管理"))
        self.tab3.setText(_translate("DantOutProt", "出库扫描"))
        self.tab4.setText(_translate("DantOutProt", "打印出货标签"))
        self.tab1.setText(_translate("DantOutProt", "产品条码管理"))
        self.out.setPlaceholderText(_translate("DantOutProt", "确认出货"))
        self.tab5.setText(_translate("DantOutProt", "出货扫描"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DantOutProt = QtWidgets.QWidget()
    ui = Ui_DantOutProt()
    ui.setupUi(DantOutProt)
    DantOutProt.show()
    sys.exit(app.exec_())


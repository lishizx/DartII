# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\Desktop\DartCodeII\CodeSet2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeSet2(object):
    def setupUi(self, CodeSet2):
        CodeSet2.setObjectName("CodeSet2")
        CodeSet2.resize(694, 320)
        CodeSet2.setMinimumSize(QtCore.QSize(0, 320))
        CodeSet2.setMaximumSize(QtCore.QSize(16777215, 360))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        CodeSet2.setWindowIcon(icon)
        CodeSet2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dat = QtWidgets.QDateTimeEdit(CodeSet2)
        self.dat.setGeometry(QtCore.QRect(20, 70, 91, 22))
        self.dat.setCalendarPopup(True)
        self.dat.setObjectName("dat")
        self.keyint = QtWidgets.QLineEdit(CodeSet2)
        self.keyint.setGeometry(QtCore.QRect(341, 198, 133, 20))
        self.keyint.setReadOnly(False)
        self.keyint.setObjectName("keyint")
        self.project = QtWidgets.QLineEdit(CodeSet2)
        self.project.setGeometry(QtCore.QRect(341, 46, 133, 20))
        self.project.setObjectName("project")
        self.tiefrom = QtWidgets.QLineEdit(CodeSet2)
        self.tiefrom.setGeometry(QtCore.QRect(341, 130, 133, 20))
        self.tiefrom.setObjectName("tiefrom")
        self.label_9 = QtWidgets.QLabel(CodeSet2)
        self.label_9.setGeometry(QtCore.QRect(159, 156, 72, 16))
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(CodeSet2)
        self.label_15.setGeometry(QtCore.QRect(480, 102, 90, 16))
        self.label_15.setObjectName("label_15")
        self.mode = QtWidgets.QLineEdit(CodeSet2)
        self.mode.setGeometry(QtCore.QRect(20, 212, 133, 20))
        self.mode.setObjectName("mode")
        self.hole = QtWidgets.QLineEdit(CodeSet2)
        self.hole.setGeometry(QtCore.QRect(341, 18, 133, 20))
        self.hole.setObjectName("hole")
        self.fromid = QtWidgets.QLineEdit(CodeSet2)
        self.fromid.setGeometry(QtCore.QRect(20, 156, 133, 20))
        self.fromid.setObjectName("fromid")
        self.picbate = QtWidgets.QLineEdit(CodeSet2)
        self.picbate.setGeometry(QtCore.QRect(341, 74, 133, 20))
        self.picbate.setObjectName("picbate")
        self.product = QtWidgets.QLineEdit(CodeSet2)
        self.product.setGeometry(QtCore.QRect(20, 44, 133, 20))
        self.product.setObjectName("product")
        self.label_8 = QtWidgets.QLabel(CodeSet2)
        self.label_8.setGeometry(QtCore.QRect(159, 128, 102, 16))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(CodeSet2)
        self.label_6.setGeometry(QtCore.QRect(116, 72, 156, 16))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(CodeSet2)
        self.label_3.setGeometry(QtCore.QRect(159, 16, 66, 16))
        self.label_3.setObjectName("label_3")
        self.label_17 = QtWidgets.QLabel(CodeSet2)
        self.label_17.setGeometry(QtCore.QRect(480, 198, 121, 16))
        self.label_17.setObjectName("label_17")
        self.machine = QtWidgets.QLineEdit(CodeSet2)
        self.machine.setGeometry(QtCore.QRect(341, 102, 133, 20))
        self.machine.setObjectName("machine")
        self.label_5 = QtWidgets.QLabel(CodeSet2)
        self.label_5.setGeometry(QtCore.QRect(159, 44, 66, 16))
        self.label_5.setObjectName("label_5")
        self.froms = QtWidgets.QLineEdit(CodeSet2)
        self.froms.setGeometry(QtCore.QRect(20, 128, 133, 20))
        self.froms.setObjectName("froms")
        self.label_12 = QtWidgets.QLabel(CodeSet2)
        self.label_12.setGeometry(QtCore.QRect(480, 18, 42, 16))
        self.label_12.setObjectName("label_12")
        self.compy = QtWidgets.QLineEdit(CodeSet2)
        self.compy.setGeometry(QtCore.QRect(20, 16, 133, 20))
        self.compy.setObjectName("compy")
        self.comboBox = QtWidgets.QComboBox(CodeSet2)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 60, 18))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(CodeSet2)
        self.label_13.setGeometry(QtCore.QRect(480, 46, 186, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(CodeSet2)
        self.label_14.setGeometry(QtCore.QRect(480, 74, 66, 16))
        self.label_14.setObjectName("label_14")
        self.label_19 = QtWidgets.QLabel(CodeSet2)
        self.label_19.setGeometry(QtCore.QRect(350, 230, 121, 16))
        self.label_19.setStyleSheet("color:red;")
        self.label_19.setObjectName("label_19")
        self.label_11 = QtWidgets.QLabel(CodeSet2)
        self.label_11.setGeometry(QtCore.QRect(159, 212, 42, 16))
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(CodeSet2)
        self.label_10.setGeometry(QtCore.QRect(159, 184, 90, 16))
        self.label_10.setObjectName("label_10")
        self.dropid = QtWidgets.QLineEdit(CodeSet2)
        self.dropid.setGeometry(QtCore.QRect(20, 184, 133, 20))
        self.dropid.setObjectName("dropid")
        self.label_16 = QtWidgets.QLabel(CodeSet2)
        self.label_16.setGeometry(QtCore.QRect(480, 130, 102, 16))
        self.label_16.setObjectName("label_16")
        self.label_7 = QtWidgets.QLabel(CodeSet2)
        self.label_7.setGeometry(QtCore.QRect(86, 100, 132, 16))
        self.label_7.setObjectName("label_7")
        self.codeshow = QtWidgets.QLineEdit(CodeSet2)
        self.codeshow.setGeometry(QtCore.QRect(20, 250, 441, 31))
        self.codeshow.setObjectName("codeshow")
        self.cunchu = QtWidgets.QPushButton(CodeSet2)
        self.cunchu.setGeometry(QtCore.QRect(480, 250, 90, 31))
        self.cunchu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cunchu.setStyleSheet("border-radius:5px;\n"
"background-color:#188eee;\n"
"color:#ffffff;\n"
"font-size:16px;")
        self.cunchu.setObjectName("cunchu")
        self.workorder = QtWidgets.QLineEdit(CodeSet2)
        self.workorder.setGeometry(QtCore.QRect(340, 160, 133, 20))
        self.workorder.setObjectName("workorder")
        self.label_18 = QtWidgets.QLabel(CodeSet2)
        self.label_18.setGeometry(QtCore.QRect(480, 160, 121, 16))
        self.label_18.setObjectName("label_18")

        self.retranslateUi(CodeSet2)
        QtCore.QMetaObject.connectSlotsByName(CodeSet2)

    def retranslateUi(self, CodeSet2):
        _translate = QtCore.QCoreApplication.translate
        CodeSet2.setWindowTitle(_translate("CodeSet2", "二维码配置"))
        self.dat.setDisplayFormat(_translate("CodeSet2", "yyyy/M/d"))
        self.label_9.setText(_translate("CodeSet2", "原料批号10位"))
        self.label_15.setText(_translate("CodeSet2", "注塑机台编号3位"))
        self.label_8.setText(_translate("CodeSet2", "原料供应商代码1位"))
        self.label_6.setText(_translate("CodeSet2", "注塑成型日期（年、月、日）"))
        self.label_3.setText(_translate("CodeSet2", "公司代码1位"))
        self.label_17.setText(_translate("CodeSet2", "产品序列号4位26进制"))
        self.label_5.setText(_translate("CodeSet2", "产品代码1位"))
        self.label_12.setText(_translate("CodeSet2", "穴号1位"))
        self.comboBox.setItemText(0, _translate("CodeSet2", "白班1"))
        self.comboBox.setItemText(1, _translate("CodeSet2", "夜班2"))
        self.label_13.setText(_translate("CodeSet2", "项目代码（B400=XX, B404=X4）2位"))
        self.label_14.setText(_translate("CodeSet2", "图纸版本2位"))
        self.label_19.setText(_translate("CodeSet2", "产品序列号不存数据库"))
        self.label_11.setText(_translate("CodeSet2", "模号3位"))
        self.label_10.setText(_translate("CodeSet2", "注塑参数代码1位"))
        self.label_16.setText(_translate("CodeSet2", "铁件供应商代码1位"))
        self.label_7.setText(_translate("CodeSet2", "班别（白班=1，夜班=2）"))
        self.cunchu.setText(_translate("CodeSet2", "保存配置"))
        self.label_18.setText(_translate("CodeSet2", "工单号"))

import style_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeSet2 = QtWidgets.QWidget()
    ui = Ui_CodeSet2()
    ui.setupUi(CodeSet2)
    CodeSet2.show()
    sys.exit(app.exec_())


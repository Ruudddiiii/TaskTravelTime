# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(915, 602)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(820, 570, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 881, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.task = QtWidgets.QWidget()
        self.task.setObjectName("task")
        self.label = QtWidgets.QLabel(self.task)
        self.label.setGeometry(QtCore.QRect(20, 10, 821, 221))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.task)
        self.listWidget.setGeometry(QtCore.QRect(600, 270, 251, 211))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.task)
        self.lineEdit.setGeometry(QtCore.QRect(30, 270, 241, 21))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.task)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.task)
        self.lcdNumber.setGeometry(QtCore.QRect(600, 240, 64, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setObjectName("lcdNumber")
        self.tabWidget.addTab(self.task, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/Pictures/Screenshot from 2024-03-07 22-28-42.png\"/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.task), _translate("Dialog", "Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Travel"))
import test_rc

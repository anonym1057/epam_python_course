# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(518, 534)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(518, 534))
        MainWindow.setMaximumSize(QtCore.QSize(518, 534))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 20, 461, 71))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 150, 361, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(400, 220, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(400, 290, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(400, 360, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(400, 430, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_step = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_step.setGeometry(QtCore.QRect(400, 150, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_step.setFont(font)
        self.pushButton_step.setObjectName("pushButton_step")
        self.disp_stack = QtWidgets.QLabel(self.centralwidget)
        self.disp_stack.setGeometry(QtCore.QRect(30, 100, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disp_stack.setFont(font)
        self.disp_stack.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.disp_stack.setFrameShape(QtWidgets.QFrame.Box)
        self.disp_stack.setFrameShadow(QtWidgets.QFrame.Raised)
        self.disp_stack.setLineWidth(1)
        self.disp_stack.setMidLineWidth(0)
        self.disp_stack.setText("")
        self.disp_stack.setScaledContents(False)
        self.disp_stack.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.disp_stack.setObjectName("disp_stack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 518, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple calculate"))
        self.pushButton_mul.setText(_translate("MainWindow", "*"))
        self.pushButton_del.setText(_translate("MainWindow", "/"))
        self.pushButton_div.setText(_translate("MainWindow", "-"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_step.setText(_translate("MainWindow", "^"))

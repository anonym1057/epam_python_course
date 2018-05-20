# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_files.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_file(object):
    def setupUi(self, Frame_file):
        Frame_file.setObjectName("Frame_file")
        Frame_file.resize(700, 76)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame_file.sizePolicy().hasHeightForWidth())
        Frame_file.setSizePolicy(sizePolicy)
        Frame_file.setMinimumSize(QtCore.QSize(700, 75))
        Frame_file.setFrameShape(QtWidgets.QFrame.Box)
        Frame_file.setFrameShadow(QtWidgets.QFrame.Raised)
        Frame_file.setLineWidth(2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Frame_file)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 671, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.retranslateUi(Frame_file)
        QtCore.QMetaObject.connectSlotsByName(Frame_file)

    def retranslateUi(self, Frame_file):
        _translate = QtCore.QCoreApplication.translate
        Frame_file.setWindowTitle(_translate("Frame_file", "Frame"))


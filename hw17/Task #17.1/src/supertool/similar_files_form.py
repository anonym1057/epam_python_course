# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'similar_files.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilesWidget(object):
    def setupUi(self, FilesWidget):
        FilesWidget.setObjectName("FilesWidget")
        FilesWidget.resize(800, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilesWidget.sizePolicy().hasHeightForWidth())
        FilesWidget.setSizePolicy(sizePolicy)
        FilesWidget.setMinimumSize(QtCore.QSize(800, 700))
        FilesWidget.setMaximumSize(QtCore.QSize(800, 700))
        self.scrollArea = QtWidgets.QScrollArea(FilesWidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 130, 751, 551))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.files_not_found = QtWidgets.QLabel(FilesWidget)
        self.files_not_found.setGeometry(QtCore.QRect(210, 120, 381, 291))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(17)
        self.files_not_found.setFont(font)
        self.files_not_found.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.files_not_found.setAlignment(QtCore.Qt.AlignCenter)
        self.files_not_found.setObjectName("files_not_found")
        self.bottun_folder = QtWidgets.QPushButton(FilesWidget)
        self.bottun_folder.setGeometry(QtCore.QRect(10, 10, 751, 61))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(12)
        self.bottun_folder.setFont(font)
        self.bottun_folder.setObjectName("bottun_folder")
        self.line_edit_selected_folder = QtWidgets.QLineEdit(FilesWidget)
        self.line_edit_selected_folder.setGeometry(QtCore.QRect(130, 80, 631, 31))
        self.line_edit_selected_folder.setReadOnly(True)
        self.line_edit_selected_folder.setObjectName("line_edit_selected_folder")
        self.label_folder = QtWidgets.QLabel(FilesWidget)
        self.label_folder.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.label_folder.setFont(font)
        self.label_folder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_folder.setObjectName("label_folder")
        self.line = QtWidgets.QFrame(FilesWidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 731, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(FilesWidget)
        QtCore.QMetaObject.connectSlotsByName(FilesWidget)

    def retranslateUi(self, FilesWidget):
        _translate = QtCore.QCoreApplication.translate
        FilesWidget.setWindowTitle(_translate("FilesWidget", "Similar files"))
        self.files_not_found.setText(_translate("FilesWidget", "Одинаковых файлов нет"))
        self.bottun_folder.setText(_translate("FilesWidget", "Выбрать папку"))
        self.label_folder.setText(_translate("FilesWidget", "Папка"))


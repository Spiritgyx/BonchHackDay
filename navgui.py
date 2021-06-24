# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\projects\hackday\navgui.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 750))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(23, 0, 954, 376))
        self.map.setStyleSheet("QLabel{\n"
"image: url(\"source/1k1e.png\");\n"
"}")
        self.map.setText("")
        self.map.setObjectName("map")
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(250, 230, 0, 0))
        self.arrow.setStyleSheet("QLabel{\n"
"image: url(\"\");\n"
"}")
        self.arrow.setText("")
        self.arrow.setObjectName("arrow")
        self.corpus = QtWidgets.QComboBox(self.centralwidget)
        self.corpus.setGeometry(QtCore.QRect(170, 410, 101, 22))
        self.corpus.setObjectName("corpus")
        self.corpus.addItem("")
        self.corpus.addItem("")
        self.cabin = QtWidgets.QSpinBox(self.centralwidget)
        self.cabin.setGeometry(QtCore.QRect(290, 410, 81, 31))
        self.cabin.setMinimum(100)
        self.cabin.setMaximum(799)
        self.cabin.setObjectName("cabin")
        self.button_check = QtWidgets.QPushButton(self.centralwidget)
        self.button_check.setGeometry(QtCore.QRect(390, 410, 121, 31))
        self.button_check.setObjectName("button_check")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Navigator"))
        self.corpus.setItemText(0, _translate("MainWindow", "1"))
        self.corpus.setItemText(1, _translate("MainWindow", "2"))
        self.button_check.setText(_translate("MainWindow", "показать"))


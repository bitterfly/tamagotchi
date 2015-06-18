# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jun 18 18:25:44 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.animal = QtWidgets.QLabel(self.centralwidget)
        self.animal.setGeometry(QtCore.QRect(120, 50, 333, 433))
        self.animal.setFrameShape(QtWidgets.QFrame.Box)
        self.animal.setText("")
        self.animal.setObjectName("animal")
        self.poo = QtWidgets.QLabel(self.centralwidget)
        self.poo.setGeometry(QtCore.QRect(130, 390, 81, 91))
        self.poo.setText("")
        self.poo.setObjectName("poo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


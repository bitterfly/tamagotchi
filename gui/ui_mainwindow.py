# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Jun 20 15:00:15 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.frame_widget = QtWidgets.QWidget(MainWindow)
        self.frame_widget.setObjectName("frame_widget")
        self.play = QtWidgets.QPushButton(self.frame_widget)
        self.play.setGeometry(QtCore.QRect(20, 570, 92, 27))
        self.play.setObjectName("play")
        self.bla1 = QtWidgets.QPushButton(self.frame_widget)
        self.bla1.setGeometry(QtCore.QRect(240, 570, 92, 27))
        self.bla1.setObjectName("bla1")
        self.bla2 = QtWidgets.QPushButton(self.frame_widget)
        self.bla2.setGeometry(QtCore.QRect(490, 570, 92, 27))
        self.bla2.setObjectName("bla2")
        self.tamagotchi_widget = TamagotchiWidget(self.frame_widget)
        self.tamagotchi_widget.setGeometry(QtCore.QRect(29, 19, 531, 531))
        self.tamagotchi_widget.setObjectName("tamagotchi_widget")
        MainWindow.setCentralWidget(self.frame_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.bla1.setText(_translate("MainWindow", "PushButton"))
        self.bla2.setText(_translate("MainWindow", "PushButton"))

from tamagotchi_widget import TamagotchiWidget

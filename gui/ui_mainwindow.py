# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jun 22 22:18:01 2015
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.canvases = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.canvases.setContentsMargins(0, 0, 0, 0)
        self.canvases.setObjectName("canvases")
        self.snake_widget = SnakeWidget(self.horizontalLayoutWidget)
        self.snake_widget.setObjectName("snake_widget")
        self.canvases.addWidget(self.snake_widget)
        self.tamagotchi_widget = TamagotchiWidget(self.horizontalLayoutWidget)
        self.tamagotchi_widget.setObjectName("tamagotchi_widget")
        self.canvases.addWidget(self.tamagotchi_widget)
        MainWindow.setCentralWidget(self.frame_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.play.setText(_translate("MainWindow", "Play"))
        self.bla1.setText(_translate("MainWindow", "PushButton"))
        self.bla2.setText(_translate("MainWindow", "PushButton"))

from snake_widget import SnakeWidget
from tamagotchi_widget import TamagotchiWidget

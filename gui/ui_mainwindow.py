# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jun 22 23:27:59 2015
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvases = QtWidgets.QHBoxLayout()
        self.canvases.setObjectName("canvases")
        self.snake_widget = SnakeWidget(self.frame_widget)
        self.snake_widget.setObjectName("snake_widget")
        self.canvases.addWidget(self.snake_widget)
        self.tamagotchi_widget = TamagotchiWidget(self.frame_widget)
        self.tamagotchi_widget.setObjectName("tamagotchi_widget")
        self.canvases.addWidget(self.tamagotchi_widget)
        self.verticalLayout.addLayout(self.canvases)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setObjectName("buttons")
        self.play = QtWidgets.QPushButton(self.frame_widget)
        self.play.setObjectName("play")
        self.buttons.addWidget(self.play)
        self.bla1 = QtWidgets.QPushButton(self.frame_widget)
        self.bla1.setObjectName("bla1")
        self.buttons.addWidget(self.bla1)
        self.bla2 = QtWidgets.QPushButton(self.frame_widget)
        self.bla2.setObjectName("bla2")
        self.buttons.addWidget(self.bla2)
        self.verticalLayout.addLayout(self.buttons)
        self.hunger_bar = QtWidgets.QProgressBar(self.frame_widget)
        self.hunger_bar.setProperty("value", 100)
        self.hunger_bar.setObjectName("hunger_bar")
        self.verticalLayout.addWidget(self.hunger_bar)
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
from snake_widget import SnakeWidget

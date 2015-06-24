# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jun 23 16:31:53 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 552)
        self.frame_widget = QtWidgets.QWidget(MainWindow)
        self.frame_widget.setObjectName("frame_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvases = QtWidgets.QHBoxLayout()
        self.canvases.setObjectName("canvases")
        self.buttons = QtWidgets.QVBoxLayout()
        self.buttons.setSpacing(0)
        self.buttons.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.buttons.setContentsMargins(0, 200, -1, -1)
        self.buttons.setObjectName("buttons")
        self.pushButton = QtWidgets.QPushButton(self.frame_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.buttons.addWidget(self.pushButton)
        self.play = QtWidgets.QPushButton(self.frame_widget)
        self.play.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setObjectName("play")
        self.buttons.addWidget(self.play)
        self.canvases.addLayout(self.buttons)
        self.snake_widget = SnakeWidget(self.frame_widget)
        self.snake_widget.setStyleSheet("border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;")
        self.snake_widget.setObjectName("snake_widget")
        self.canvases.addWidget(self.snake_widget)
        self.tamagotchi_widget = TamagotchiWidget(self.frame_widget)
        self.tamagotchi_widget.setObjectName("tamagotchi_widget")
        self.canvases.addWidget(self.tamagotchi_widget)
        self.verticalLayout.addLayout(self.canvases)
        self.hunger_bar = QtWidgets.QProgressBar(self.frame_widget)
        self.hunger_bar.setProperty("value", 100)
        self.hunger_bar.setObjectName("hunger_bar")
        self.verticalLayout.addWidget(self.hunger_bar)
        self.progressBar = QtWidgets.QProgressBar(self.frame_widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.frame_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "another"))
        self.play.setText(_translate("MainWindow", "Play"))

from snake_widget import SnakeWidget
from tamagotchi_widget import TamagotchiWidget

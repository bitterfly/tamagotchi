#Самия външен прозорец
import sys
import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
from ui_mainwindow import Ui_MainWindow

script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(script_directory,
                                   os.pardir))
sys.path.append(parent_directory)

from core.tamagotchi import Tamagotchi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tamagotchi = Tamagotchi()
        self.ui.tamagotchi_widget.tamagotchi = self.tamagotchi

        #Свързване на уиджета на снейка при натискане на бутон плей
        self.ui.play.clicked.connect(self.snake_game)

        #Скриване на снейк - уиджет и фокус на тамагочи
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

        self.ui.snake_widget.dead_signal.connect(self.end_snake_game)

        #Таймерът, с който се отмерва времето на самото животно
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.second_pass)
        self.timer.start(100)

    def second_pass(self):
        self.tamagotchi.second_pass()

    @QtCore.pyqtSlot()
    def end_snake_game(self):
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

    def set_focus(self, new_widget, old_widget):
        old_widget.hide()
        new_widget.show()
        new_widget.setFocus()

    @QtCore.pyqtSlot()
    def snake_game(self):
        #скрива се тамагочито и се показва змията
        self.set_focus(self.ui.snake_widget, self.ui.tamagotchi_widget)

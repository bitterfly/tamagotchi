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
        self.ui.cure.clicked.connect(self.cure)

        #Скриване на снейк - уиджет и фокус на тамагочи
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

        self.ui.snake_widget.dead_signal.connect(self.end_snake_game)
        self.ui.snake_widget.coin_signal.connect(self.add_coins)

        #Таймерът, с който се отмерва времето на самото животно
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.second_pass)
        self.timer.start(100)
        self.ui.coin.setPixmap(self.ui.tamagotchi_widget.coin_image)

    @QtCore.pyqtSlot()
    def second_pass(self):
        self.tamagotchi.second_pass()
        self.update_bars()

    def update_bars(self):
        self.ui.food_bar.setValue(self.tamagotchi.stats["food"])
        self.ui.hygiene_bar.setValue(self.tamagotchi.stats["hygiene"])
        self.ui.happiness_bar.setValue(self.tamagotchi.stats["happiness"])
        self.ui.energy_bar.setValue(self.tamagotchi.stats["energy"])
        self.ui.health_bar.setValue(self.tamagotchi.stats["health"])

    @QtCore.pyqtSlot()
    def end_snake_game(self):
        self.tamagotchi.is_playing = False
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

    @QtCore.pyqtSlot()
    def add_coins(self):
        self.ui.number_of_coins.setText(str(int(self.ui.number_of_coins.text()) + 1))

    def set_focus(self, new_widget, old_widget):
        old_widget.hide()
        new_widget.show()
        new_widget.setFocus()

    def cure(self):
        self.tamagotchi.stats["health"] = 100
        self.tamagotchi.is_sick == False

    @QtCore.pyqtSlot()
    def snake_game(self):
        #скрива се тамагочито и се показва змията
        self.ui.snake_widget.newGame()
        self.tamagotchi.is_playing = True
        self.set_focus(self.ui.snake_widget, self.ui.tamagotchi_widget)

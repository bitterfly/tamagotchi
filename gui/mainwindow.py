#Самия външен прозорец
import sys
import os
import pickle
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
from ui_mainwindow import Ui_MainWindow
from xdg.BaseDirectory import xdg_config_home

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
        #load existing tamagotchi if any:
        if os.path.exists(os.path.join(xdg_config_home, 'tamagotchi.pickle')):
            with open(os.path.join(xdg_config_home, 'tamagotchi.pickle'), 'rb') as output_file:
                self.tamagotchi = pickle.load(output_file)
                seconds_since_save = (datetime.now() - pickle.load(output_file)).total_seconds()
                self.tamagotchi.second_pass(seconds_since_save)
                self.update_bars()
        else:
            self.tamagotchi = Tamagotchi()
        self.ui.tamagotchi_widget.tamagotchi = self.tamagotchi

        #Свързване на уиджета на снейка при натискане на бутон плей
        self.ui.play.clicked.connect(self.snake_game)
        self.ui.cure.clicked.connect(self.cure)
        self.ui.save.clicked.connect(self.save)

        #Скриване на снейк - уиджет и фокус на тамагочи
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

        self.ui.snake_widget.dead_signal.connect(self.end_snake_game)
        self.ui.snake_widget.coin_signal.connect(self.add_coins)

        #Таймерът, с който се отмерва времето на самото животно
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.second_pass)
        self.timer.start(100)
        self.ui.coin.setPixmap(self.ui.tamagotchi_widget.coin_image)
        #Set coins
        self.ui.number_of_coins.setText(str(self.tamagotchi.money))

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
        self.tamagotchi.money += 1
        self.ui.number_of_coins.setText(str(self.tamagotchi.money))

    def set_focus(self, new_widget, old_widget):
        old_widget.hide()
        new_widget.show()
        new_widget.setFocus()

    @QtCore.pyqtSlot()
    def cure(self):
        self.tamagotchi.stats["health"] = 100
        self.tamagotchi.is_sick == False

    @QtCore.pyqtSlot()
    def save(self):
        with open(os.path.join(xdg_config_home, 'tamagotchi.pickle'), 'wb') as output_file:
            pickle.dump(self.tamagotchi, output_file)
            pickle.dump(datetime.now(), output_file)
        if self.tamagotchi.is_playing:
            self.snake_widget.setFocus()
    @QtCore.pyqtSlot()
    def snake_game(self):
        if not self.tamagotchi.is_playing:
            #скрива се тамагочито и се показва змията
            self.ui.snake_widget.newGame()
            self.tamagotchi.is_playing = True
            self.set_focus(self.ui.snake_widget, self.ui.tamagotchi_widget)

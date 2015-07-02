#Самия външен прозорец
import sys
import os
import pickle
import json
from PyQt5 import QtWidgets
from datetime import datetime
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore
from PyQt5 import QtGui
from ui_mainwindow import Ui_MainWindow
from xdg.BaseDirectory import xdg_config_home

script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(script_directory,
                                   os.pardir))
resource_directory = os.path.join(script_directory, "resources")
extras_directory = os.path.join(resource_directory, "extra")
sys.path.append(parent_directory)
from core.tamagotchi import Tamagotchi

class ClickableLabel(QLabel):
    clicked = QtCore.pyqtSignal()
    item = None
    def mousePressEvent(self, event):
        self.clicked.emit()


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

        #Свързване на всички бутони:
        self.connect_buttons()

        #Скриване на снейк - уиджет и фокус на тамагочи
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

        self.ui.snake_widget.dead_signal.connect(self.end_snake_game)
        self.ui.snake_widget.coin_signal.connect(self.add_coins)

        #****
        self.ui.tamagotchi_widget.load_resources()
        #****
        #Таймерът, с който се отмерва времето на самото животно
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.second_pass)
        self.timer.start(100)
        self.ui.coin.setPixmap(self.ui.tamagotchi_widget.coin_image)

        #Set coins
        self.ui.number_of_coins.setText(str(self.tamagotchi.money))
        self.load_store()


    def connect_buttons(self):
        self.ui.play.clicked.connect(self.snake_game)
        self.ui.sleep.clicked.connect(self.sleep)
        self.ui.store.clicked.connect(self.open_store)
        self.ui.save.clicked.connect(self.save)


    def buy_item(self):
        item = self.sender().item
        self.tamagotchi.apply(item["stats"])
        if self.tamagotchi.stats["health"] == 100:
            self.tamagotchi.cure()

    def load_store(self):
        self.store_labels = []
        #Четат се айтемите от файл в същата директория
        with open(os.path.join(script_directory, 'items'), 'r') as output_file:
            self.items = json.load(output_file)

        #Създават се по два лейбъла за всеки обект: картинка и текст
        #И се подреждат в грид-а на widget-a

        for item in self.items:
            text_label = ClickableLabel()
            image_label = ClickableLabel()
            image = QtGui.QPixmap(os.path.join(extras_directory, item["image"]))
            text_label.item = item
            text_label.clicked.connect(self.buy_item)
            image_label.item = item
            image_label.clicked.connect(self.buy_item)

            image_label.setPixmap(image.scaled(100, 100, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            text_label.setText("NAME: " + item["name"] + ": " + str(item["price"]) + "p")
            for key, value in item["stats"].items():
                if value != 0:
                    text_label.setText(text_label.text() + "\n" + str(key) + ": " + str(value))

            self.store_labels.append((text_label, image_label))

            self.ui.store_frame.layout().addWidget(text_label, item["coordinates"][0], item["coordinates"][1])
            self.ui.store_frame.layout().addWidget(image_label, item["coordinates"][0] + 1, item["coordinates"][1])
            self.check_prices()

    def check_prices(self):
        for item in self.store_labels:
            if item[0].item["price"] > self.tamagotchi.money:
                item[0].setEnabled(False)
                item[1].setEnabled(False)
            else:
                item[0].setEnabled(True)
                item[1].setEnabled(True)

    def change_mode(self, mode):
        self.ui.tamagotchi_widget.tamagotchi_images = mode

    @QtCore.pyqtSlot()
    def sleep(self):
        if self.tamagotchi.is_sleeping:
            self.tamagotchi.is_sleeping = False
            if self.tamagotchi.is_sick:
                self.change_mode(self.ui.tamagotchi_widget.tamagotchi_sick)
            else:
                self.change_mode(self.ui.tamagotchi_widget.tamagotchi_normal)
        else:
            self.tamagotchi.is_sleeping = True
            self.change_mode(self.ui.tamagotchi_widget.tamagotchi_sleep)

    @QtCore.pyqtSlot()
    def second_pass(self):
        self.tamagotchi.second_pass()
        if not self.tamagotchi.is_sleeping:
            if self.tamagotchi.is_sick:
                self.change_mode(self.ui.tamagotchi_widget.tamagotchi_sick)
            else:
                self.change_mode(self.ui.tamagotchi_widget.tamagotchi_normal)
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
        self.ui.buttons_2.setEnabled(True)
        self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)

    @QtCore.pyqtSlot()
    def add_coins(self):
        self.tamagotchi.money += 1
        self.ui.number_of_coins.setText(str(self.tamagotchi.money))
        self.check_prices()

    def set_focus(self, new_widget, old_widget, unused_widget=None):
        old_widget.hide()
        if not unused_widget:
            unused_widget = self.ui.store_frame
        unused_widget.hide()
        new_widget.show()
        new_widget.setFocus()

    @QtCore.pyqtSlot()
    def open_store(self):
        if self.ui.store_frame.isVisible():
           self.set_focus(self.ui.tamagotchi_widget, self.ui.snake_widget)
        else:
            self.set_focus(self.ui.store_frame, self.ui.tamagotchi_widget, self.ui.snake_widget)

    @QtCore.pyqtSlot()
    def save(self):
        with open(os.path.join(xdg_config_home, 'tamagotchi.pickle'), 'wb') as output_file:
            pickle.dump(self.tamagotchi, output_file)
            pickle.dump(datetime.now(), output_file)

    @QtCore.pyqtSlot()
    def snake_game(self):
        if not self.tamagotchi.is_playing:
            #скрива се тамагочито и се показва змията
            self.ui.snake_widget.newGame()
            self.ui.buttons_2.setEnabled(False)
            self.tamagotchi.is_playing = True
            self.set_focus(self.ui.snake_widget, self.ui.tamagotchi_widget)

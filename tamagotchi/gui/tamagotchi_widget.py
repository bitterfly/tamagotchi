#Файлът с неща за самия уиджет, в който с qпейнтър ще има стъф.

import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore
from random import randint
from collections import defaultdict

script_directory = os.path.dirname(os.path.abspath(__file__))
resource_path = os.path.join(script_directory, "resources")
ewok_directory = os.path.join(resource_path, "ewok")
extra_directory = os.path.join(resource_path, "extra")
poo_directory = os.path.join(extra_directory, "poo")
normal_mode = os.path.join(ewok_directory, "normal")
sick_mode = os.path.join(ewok_directory, "sick")
sleep_mode = os.path.join(ewok_directory, "sleep")

class TamagotchiWidget(QWidget):
    def __init__(self, parent):
        super(TamagotchiWidget, self).__init__(parent)

        self.image_number = 0
        self.poo_image_number = 0

        #Sets the timer which changes the images
        self.frame_timer = QtCore.QTimer(self)
        self.frame_timer.timeout.connect(self.next_image)
        self.frame_timer.start(50)
        self.poo_coordinates = defaultdict(self.place_random_poo)
        self.show()

    #Places a poo in the lower 2/3 of the screen
    def place_random_poo(self):
        return (
            randint(0,
                    self.size().width() - 100),
            randint((2 * self.size().height()) // 3,
                     self.size().height() - 100)
        )

    #Load every image and sets current mode - sick, normal, sleeping
    #and the appropriate background
    def load_resources(self):
        self.tamagotchi_images = []
        self.tamagotchi_normal = []
        self.tamagotchi_sick = []
        self.tamagotchi_sleep = []
        self.poo_images = []
        self.background_day = QtGui.QPixmap(
            os.path.join(extra_directory, "background.png")
        )
        self.background_night = QtGui.QPixmap(
            os.path.join(extra_directory, "background_night.png")
        )
        self.background = self.background_day
        self.grave_image = QtGui.QPixmap(
            os.path.join(extra_directory, "rip.jpg")
        )
        self.coin_image = QtGui.QPixmap(os.path.
            join(extra_directory, "coin.png")).scaled(90, 90)

        for file in sorted(os.listdir(poo_directory)):
            self.poo_images.append(
                QtGui.QPixmap(os.path.join(poo_directory, file))
            )

        for file in sorted(os.listdir(normal_mode)):
            self.tamagotchi_normal.append(QtGui.QPixmap(os.path.join(normal_mode, file)))

        for file in sorted(os.listdir(sick_mode)):
            self.tamagotchi_sick.append(
                QtGui.QPixmap(os.path.join(sick_mode, file))
            )

        for file in sorted(os.listdir(sleep_mode)):
            self.tamagotchi_sleep.append(QtGui.QPixmap(
                os.path.join(sleep_mode, file))
            )
        if self.tamagotchi.is_sleeping:
            self.tamagotchi_images = self.tamagotchi_sleep
            self.background = self.background_night
        else:
            if self.tamagotchi.is_sick:
                self.tamagotchi_images = self.tamagotchi_sick
            else:
                self.tamagotchi_images = self.tamagotchi_normal
                self.background = self.background_day

    @QtCore.pyqtSlot()
    def next_image(self):
        self.image_number += 1
        self.poo_image_number += 1
        if self.image_number >= len(self.tamagotchi_images) - 1:
            self.image_number = 0
        if self.poo_image_number >= len(self.poo_images) - 1:
            self.poo_image_number = 0
        self.repaint()

    def draw_tamagotchi(self, canvas):
        image = self.tamagotchi_images[self.image_number]
        canvas.drawPixmap(0, 0, image.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def draw_extra(self, canvas):
        if self.tamagotchi.number_of_poo:
            for poo in range(self.tamagotchi.number_of_poo):
                image = self.poo_images[self.poo_image_number]
                canvas.drawPixmap(self.poo_coordinates[poo][0], self.poo_coordinates[poo][1],
                    image.scaled(
                        100, 100, QtCore.Qt.KeepAspectRatio,
                        QtCore.Qt.SmoothTransformation)
                    )


    def draw_grave(self, canvas):
        canvas.drawPixmap(0, 0, self.grave_image.scaled(
            self.size(), QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation)
        )

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.drawPixmap(0, 0, self.background.scaled(
            self.size(), QtCore.Qt.IgnoreAspectRatio,
            QtCore.Qt.SmoothTransformation)
        )
        if self.tamagotchi.is_dead:
            self.draw_grave(canvas)
        else:
            self.draw_extra(canvas)
            self.draw_tamagotchi(canvas)
        canvas.end()




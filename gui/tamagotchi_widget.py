#Файлът с неща за самия уиджет, в който с qпейнтър ще има стъф.

import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore

script_directory = os.path.dirname(os.path.abspath(__file__))
resource_path = os.path.join(script_directory, "resources")

class TamagotchiWidget(QWidget):
    def __init__(self, parent):
        super(TamagotchiWidget, self).__init__(parent)
        self.load_resources("ewok1")
        self.image_number = 0

        #Таймерът, който анимира смяната на картинките
        self.frame_timer = QtCore.QTimer(self)
        self.frame_timer.timeout.connect(self.next_image)
        self.frame_timer.start(50)
        self.show()

    def load_resources(self, directory):
        self.tamagotchi_images = []
        extra_directory = os.path.join(resource_path, "extra")
        self.grave_image = QtGui.QPixmap(os.path.join(extra_directory, "rip.jpg"))
        self.coin_image = QtGui.QPixmap(os.path.join(extra_directory, "coin.png")).scaled(100, 100)
        ewok_directory = os.path.join(resource_path, directory)
        for file in sorted(os.listdir(ewok_directory)):
            self.tamagotchi_images.append(QtGui.QPixmap(os.path.join(ewok_directory, file)))

    @QtCore.pyqtSlot()
    def next_image(self):
        self.image_number += 1
        if self.image_number >= len(self.tamagotchi_images) - 1:
            self.image_number = 0
        self.repaint()

    def draw_tamagotchi(self, canvas):
        image = self.tamagotchi_images[self.image_number]
        canvas.drawPixmap(0, 0, image.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def draw_extra(self, canvas):
        pass

    def draw_grave(self, canvas):
        canvas.drawPixmap(0, 0, self.grave_image.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        canvas.setPen(QtCore.Qt.NoPen)
        if self.tamagotchi.is_dead:
            self.draw_grave(canvas)
        else:
            self.draw_extra(canvas)
            self.draw_tamagotchi(canvas)
        canvas.end()




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
        self.frame_timer.start(5)
        self.show()

    def load_resources(self, directory):
        self.tamagotchi_images = []
        full_path = os.path.join(resource_path, directory)
        for file in sorted(os.listdir(full_path)):
            self.tamagotchi_images.append(QtGui.QPixmap(os.path.join(full_path, file)))

    @QtCore.pyqtSlot()
    def next_image(self):
        self.image_number += 1
        if self.image_number >= len(self.tamagotchi_images) - 1:
            self.image_number = 0
        self.repaint()

    def draw_tamagotchi(self, canvas):
        canvas.setPen(QtCore.Qt.black)
        image = self.tamagotchi_images[self.image_number]
        canvas.drawPixmap(0, 0, image.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def draw_extra(self, canvas):
        pass

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        self.draw_tamagotchi(canvas)
        self.draw_extra(canvas)
        canvas.end()






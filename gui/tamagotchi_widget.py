#Файлът с неща за самия уиджет, в който с qпейнтър ще има стъф.

import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore
script_directory = os.path.dirname(os.path.abspath(__file__))
resource_path = os.path.join(script_directory, "resources")


class TamagotchiWidget(QWidget):
    def __init__(self, parent):
        super(TamagotchiWidget, self).__init__(parent)
        self.loadResources()
        self.image_number = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.nextImage)
        self.timer.start(5)
        self.show()

    def loadResources(self):
        self.tamagotchi_images = []
        full_path = os.path.join(resource_path, "ewok1")
        for file in sorted(os.listdir(full_path)):
            self.tamagotchi_images.append(QtGui.QPixmap(os.path.join(full_path, file)))

    @QtCore.pyqtSlot()
    def nextImage(self):
        self.image_number += 1
        if self.image_number >= len(self.tamagotchi_images):
            self.image_number = 0
        self.repaint()


    def drawTamagotchi(self, canvas):
        canvas.setPen(QtCore.Qt.black)
        image = self.tamagotchi_images[self.image_number]
        canvas.drawPixmap(0, 0, image.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def drawExtra(self, canvas):
        pass

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        self.drawTamagotchi(canvas)
        self.drawExtra(canvas)
        canvas.end()






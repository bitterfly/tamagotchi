from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resources()

    def resources(self):
        ewok = QMovie("/home/do/geek/tamagotchi/gui/source/ewok.gif")
        poo = QMovie("/home/do/geek/tamagotchi/gui/source/poo.gif")
        self.ui.animal.setMovie(ewok)
        self.ui.poo.setMovie(poo)
        poo.setScaledSize(self.ui.poo.size())
        poo.setSpeed(600)
        ewok.setScaledSize(self.ui.animal.size())
        ewok.start()
        poo.start()


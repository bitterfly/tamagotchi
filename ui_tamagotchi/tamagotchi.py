from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
from ui_tamagotchi import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ewok = QMovie("/home/do/geek/tamagotchi/ui_tamagotchi/source/ewok.gif")
        ewok.setScaledSize(self.ui.animal.size())
        poo = QMovie("/home/do/geek/tamagotchi/ui_tamagotchi/source/poo.gif")
        poo.setScaledSize(self.ui.poo.size())
        self.ui.animal.setMovie(ewok)
        self.ui.poo.setMovie(poo)
        poo.setSpeed(600)
        ewok.start()
        poo.start()

#Самия външен прозорец
import sys
import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
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


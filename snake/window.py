from PyQt5.QtWidgets import QMainWindow
from ui_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pause.setText('')
        self.ui.snake_widget.pause_label = self.ui.pause
        self.ui.snake_widget.setFocus()

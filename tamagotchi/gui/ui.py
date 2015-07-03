import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
script_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_directory)
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

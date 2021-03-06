import sys
import time
import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5 import QtCore
from random import randrange

script_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(script_directory,
                                   os.pardir))
#sys.path.append(parent_directory)
sys.path.append(os.path.join(parent_directory, "snake"))
#sys.path.append(script_directory)
from snake import Snake

class SnakeWidget(QWidget):
    coin_signal = QtCore.pyqtSignal()
    dead_signal = QtCore.pyqtSignal()
    def __init__(self, parent):
        super(SnakeWidget, self).__init__(parent)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.move)
        self.newGame()
        self.colors = [QtGui.QColor(255, 0, 0, 255),
                       QtGui.QColor(255, 255, 0, 255),
                       QtGui.QColor(0, 0, 255, 255),
                       QtGui.QColor(0, 255, 0, 255)]

    def newGame(self):
        self.snake = Snake()
        self.is_paused = False
        self.show()
        self.timer.start(50)

    def resizeEvent(self, event):
        self._cell_height = self.size().height() // self.snake.field_height
        self._cell_width = self.size().width() // self.snake.field_width

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        self.drawFood(canvas)
        self.drawSnake(canvas)
        canvas.end()

    def keyPressEvent(self, event):
        directions = {QtCore.Qt.Key_Down: "down",
                      QtCore.Qt.Key_Up: "up",
                      QtCore.Qt.Key_Right: "right",
                      QtCore.Qt.Key_Left: "left"}
        if self.snake.dead and event.key() == QtCore.Qt.Key_N:
            self.newGame()

        if event.key() == QtCore.Qt.Key_Escape:
            self.die()
            self.hide()

        if event.key() == QtCore.Qt.Key_Space:
            self.pause()

        if not self.is_paused and event.key() in directions.keys():
            self.snake.key_press(directions[event.key()])

    def pause(self):
        if not self.snake.dead:
            if self.is_paused:
                self.pause_label.hide()
                self.is_paused = False
                self.timer.start()
            else:
                self.pause_label.show()
                self.is_paused = True
                self.timer.stop()

    def drawSnake(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        for segment in self.snake.snake_body:
            canvas.setBrush(QtGui.QColor(255, 80, 0, 255))
            canvas.drawRect((segment[0] * self.size().width()) // self.snake.field_width,
                            (segment[1] * self.size().height()) // self.snake.field_height,
                            self._cell_width + 1, self._cell_height + 1)

    def drawFood(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.setBrush(QtGui.QColor(0, 80, 255, 255))
        canvas.drawEllipse(
            (self.snake.food_coordinates[0] * self.size().width()) // self.snake.field_width,
            (self.snake.food_coordinates[1] * self.size().height()) // self.snake.field_height,
            self._cell_width, self._cell_height
            )

    @QtCore.pyqtSlot()
    def move(self):
        if self.snake.dead:
            self.die()
        score = self.snake.score
        self.snake.move()
        if self.snake.score > score:
            self.coin_signal.emit()
        self.repaint()

    def die(self):
        self.timer.stop()
        self.snake.die()
        self.dead_signal.emit()

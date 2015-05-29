from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore
import sys, time
from random import randrange
from core_snake import Snake

class SnakeGUI(QWidget):
    def __init__(self, parent):
        super(SnakeGUI, self).__init__(parent)
        self.snake = Snake()
        self.newGame()
        self.colors = [QtGui.QColor(255, 0, 0, 255), QtGui.QColor(255, 255, 0, 255), QtGui.QColor(0, 0, 255, 255), QtGui.QColor(0, 255, 0, 255)]


    def newGame(self):
        self.is_paused = False
        self.show()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.move)
        self.timer.start(75)

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
                self.pause_label.setText("")
                self.is_paused = False
                self.timer.start()
            else:

                self.is_paused = True
                self.pause_label.setText("Press Space or arrows to continue")
                self.timer.stop()
                print(self.snake.score)

    def drawSnake(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        for segment in self.snake.snake_body:
            canvas.setBrush(QtGui.QColor(255, 80, 0, 255))
            canvas.drawRect(segment[0] * self._cell_width, segment[1] * self._cell_height, self._cell_width, self._cell_height)

    def drawFood(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.setBrush(QtGui.QColor(0, 80, 255, 255))
        canvas.drawEllipse(self.snake.food_coordinates[0] * self._cell_width, self.snake.food_coordinates[1] * self._cell_height, self._cell_width, self._cell_height)

    @QtCore.pyqtSlot()
    def move(self):
        self.snake.move()
        self.repaint()

    def die(self):
        self.timer.stop()
        self.dead = True
        self.snake.die()

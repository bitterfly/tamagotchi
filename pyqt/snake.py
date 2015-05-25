from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui, QtCore
import sys, time
from random import randrange

class Snake(QWidget):
    def __init__(self, parent):
        super(Snake, self).__init__(parent)
        self.field_height = 50
        self.field_width = 75
        self.newGame()
        self.colors = [QtGui.QColor(255, 0, 0, 255), QtGui.QColor(255, 255, 0, 255), QtGui.QColor(0, 0, 255, 255), QtGui.QColor(0, 255, 0, 255)]

    def newGame(self):
        self.show()
        self.score = 0
        self.x = self.field_width // 2;
        self.y = self.field_height // 2;
        self.direction = (1, 0)
        self.timer = QtCore.QTimer(self)
        self.snake_body = [(self.x, self.y), (self.x - 1, self.y), (self.x - 2, self.y)]
        self.is_paused = False
        self.dead = False
        self.timer.timeout.connect(self.move)
        self.timer.start(75)
        self.food_coordinates = (42, 42)

    def resizeEvent(self, event):
        self._cell_height = self.size().height() // self.field_height
        self._cell_width = self.size().width() // self.field_width

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        self.drawFood(canvas)
        self.drawSnake(canvas)
        canvas.end()

    def keyPressEvent(self, event):
        if self.dead and event.key() == QtCore.Qt.Key_N:
            self.newGame()
        if self.is_paused and (event.key() == QtCore.Qt.Key_Down or event.key() == QtCore.Qt.Key_Up or event.key() == QtCore.Qt.Key_Left or event.key() == QtCore.Qt.Key_Right):
            self.is_paused = False
            self.timer.start()
        if event.key() == QtCore.Qt.Key_Space:
            self.pause()
        if not self.is_paused:
            if event.key() == QtCore.Qt.Key_Down and (self.last_direction != (0, 1) and self.last_direction != (0, -1)):
                self.direction = (0, 1)
            elif event.key() == QtCore.Qt.Key_Up and (self.last_direction != (0, 1) and self.last_direction != (0, -1)):
                self.direction = (0, -1)
            elif event.key() == QtCore.Qt.Key_Right and (self.last_direction != (1, 0) and self.last_direction != (-1, 0)):
                self.direction = (1, 0)
            elif event.key() == QtCore.Qt.Key_Left and (self.last_direction != (1, 0) and self.last_direction != (-1, 0)):
                self.direction = (-1, 0)
        if event.key() == QtCore.Qt.Key_Escape:
            self.die()
            self.hide()

    def pause(self):
        if not self.dead:
            if self.is_paused:
                self.pause_label.setText("")
                self.is_paused = False
                self.timer.start()
            else:

                self.is_paused = True
                self.pause_label.setText("Press Space or arrows to continue")
                self.timer.stop()
                print(self.score)

    def drawSnake(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        for segment in self.snake_body:
            canvas.setBrush(QtGui.QColor(255, 80, 0, 255))
            canvas.drawRect(segment[0] * self._cell_width, segment[1] * self._cell_height, self._cell_width, self._cell_height)

    def drawFood(self, canvas):
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.setBrush(QtGui.QColor(0, 80, 255, 255))
        canvas.drawEllipse(self.food_coordinates[0] * self._cell_width, self.food_coordinates[1] * self._cell_height, self._cell_width, self._cell_height)


    def step(self, direction):
        self.last_direction = self.direction
        new_x = (self.x + direction[0]) % self.field_width
        new_y = (self.y + direction[1]) % self.field_height
        if (new_x,new_y) in self.snake_body:
            self.die()
        else:
            self.snake_body.insert(0, (new_x, new_y))
            self.x = new_x
            self.y = new_y
            if (self.x, self.y) == self.food_coordinates:
                self.food_coordinates = (randrange(0, self.field_width), randrange(0, self.field_height))
                self.score += 1
            else:
                self.snake_body.pop()

    @QtCore.pyqtSlot()
    def move(self):
        self.step(self.direction)
        self.repaint()

    def die(self):
        self.timer.stop()
        self.dead = True
        self.maxscore = self.score
        print(self.score)

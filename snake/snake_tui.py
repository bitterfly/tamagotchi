import sys, time
from core_snake import Snake
from threading import Thread
from getch import getch
import termios
from curses import wrapper, curs_set, start_color, init_pair, color_pair, use_default_colors, endwin, echo, nocbreak

class SnakeTUI:
    def __init__(self, stdscr):
        self.screen = stdscr
        self.snake = Snake(self.screen.getmaxyx()[1] // 2 - 1, self.screen.getmaxyx()[0])
        self.screen.nodelay(1)
        curs_set(0)
        start_color()
        use_default_colors()
        init_pair(1, -1, 6)
        init_pair(2, 3, -1)
        self.new_game()

    def new_game(self):
        directions = {258: "down", 259: "up", 260: "left", 261: "right"}
        while(True):
            if self.snake.dead:
                break
            time.sleep(0.075)
            current_button = self.screen.getch()
            if current_button == 27:
                break
            elif current_button in directions.keys():
                self.snake.key_press(directions[current_button])
            self.snake.move()
            self.draw_board()
        self.die()

    def die(self):
        self.screen.clear()
        self.screen.addstr(10, 10, "GAME OVER")
        self.screen.addstr(11, 10, "Score: " + str(self.snake.score))
        self.screen.refresh()
        time.sleep(2)
        self.snake.die()

    def draw_board(self):
        self.screen.clear()
        self.screen.addstr(self.snake.food_coordinates[1], self.snake.food_coordinates[0] * 2, "⬤", color_pair(2))
        for x, y in self.snake.snake_body:
            self.screen.addstr(y, x * 2, "  ", color_pair(1))
        self.screen.refresh()

if __name__ == '__main__':
    wrapper(SnakeTUI)

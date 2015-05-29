import sys, time
from random import randrange

class Snake:
    def __init__(self, width=75, height=50):
        self.field_height = height
        self.field_width = width
        self.score = 0
        self.maxscore = 0
        self.x = self.field_width // 2;
        self.y = self.field_height // 2;
        self.direction = (1, 0)
        self.last_direction = (1, 0)
        self.snake_body = [(self.x, self.y), (self.x - 1, self.y), (self.x - 2, self.y)]
        self.dead = False
        self.put_food()

    def put_food(self):
        self.food_coordinates = (randrange(0, self.field_width), randrange(0, self.field_height))

    def key_press(self, key):
        if key == "down" and (self.last_direction != (0, 1) and self.last_direction != (0, -1)):
            self.direction = (0, 1)
        elif key == "up" and (self.last_direction != (0, 1) and self.last_direction != (0, -1)):
            self.direction = (0, -1)
        elif key == "right" and (self.last_direction != (1, 0) and self.last_direction != (-1, 0)):
            self.direction = (1, 0)
        elif key == "left" and (self.last_direction != (1, 0) and self.last_direction != (-1, 0)):
            self.direction = (-1, 0)

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
                self.put_food()
                self.score += 1
            else:
                self.snake_body.pop()

    def move(self):
        self.step(self.direction)

    def die(self):
        self.dead = True
        if self.score > self.maxscore:
            self.maxscore = self.score
        return self.maxscore

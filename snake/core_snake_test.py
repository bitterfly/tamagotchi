import unittest
from core_snake import Snake


class TestSnake(unittest.TestCase):
    def test_init(self):
        snake = Snake()
        self.assertEqual(snake.field_height, 50)
        self.assertEqual(snake.field_width, 75)
        self.assertEqual(snake.score, 0)
        self.assertEqual(snake.maxscore, 0)
        self.assertEqual(snake.x, 37)
        self.assertEqual(snake.y, 25)
        self.assertEqual(snake.direction, (1, 0))
        self.assertEqual(snake.last_direction, (1, 0))
        self.assertEqual(snake.snake_body, [(37, 25), (36, 25), (35, 25)])
        self.assertFalse(snake.dead)

    def test_init_parameters(self):
        snake = Snake(width=100, height=100)
        self.assertEqual(snake.field_height, 100)
        self.assertEqual(snake.field_width, 100)
        self.assertEqual(snake.x, 50)
        self.assertEqual(snake.y, 50)
        self.assertEqual(snake.snake_body, [(50, 50), (49, 50), (48, 50)])

    def test_init_small_field(self):
        snake = Snake(width=0, height=1000)
        self.assertEqual(snake.field_height, 50)
        self.assertEqual(snake.field_width, 75)

    def test_key_press_moves(self):
        snake = Snake()
        snake.key_press('up')
        self.assertEqual(snake.last_direction, (1, 0))
        self.assertEqual(snake.direction, (0, -1))

    def test_key_press_stays(self):
        snake = Snake()
        snake.last_direction = (-1, 0)
        snake.direction = (-1, 0)
        snake.key_press("right")
        self.assertEqual(snake.last_direction, (-1, 0))
        self.assertEqual(snake.direction, (-1, 0))

    def test_step_dies(self):
        snake = Snake()
        snake.step((0, 0))
        self.assertTrue(snake.dead)

    def test_step_pushback(self):
        snake = Snake(width=100, height=100)
        snake.food_coordinates = (0, 0)
        snake.step((1, 0))
        self.assertEqual(snake.snake_body, [(51, 50), (50, 50), (49, 50)])
        self.assertEqual(snake.score, 0)
        self.assertEqual(snake.x, 51)
        self.assertEqual(snake.y, 50)

    def test_step_eating(self):
        snake = Snake(width=100, height=100)
        snake.food_coordinates = (51, 50)
        snake.step((1, 0))
        self.assertEqual(snake.snake_body, [(51, 50), (50, 50),
                                            (49, 50), (48, 50)])
        self.assertEqual(snake.score, 1)
        self.assertTrue(snake.food_coordinates not in snake.snake_body)

if __name__ == '__main__':
    unittest.main()

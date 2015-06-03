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
        self.assertEqual(snake.last_direction, (1,0))
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
        snake = Snake(width = 0, height = 1000)
        self.assertEqual(snake.field_height, 50)
        self.assertEqual(snake.field_width, 75)

if __name__ == '__main__':
    unittest.main()








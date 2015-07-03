import unittest
from tamagotchi import Tamagotchi
from item import Item

class TestTamagotchi(unittest.TestCase):
    def test_init(self):
        tamagotchi = Tamagotchi()
        self.assertEqual(tamagotchi.stats["food"], 100)
        self.assertEqual(tamagotchi.stats["happiness"], 100)
        self.assertEqual(tamagotchi.stats["hygiene"], 100)
        self.assertEqual(tamagotchi.stats["health"], 100)
        self.assertEqual(tamagotchi.stats["energy"], 100)
        self.assertEqual(tamagotchi.stats["age"], 0)

    def test_apply_exceding(self):
        tamagotchi = Tamagotchi()
        item = Item(100, 0, 0, 0, 0, 0)
        tamagotchi.apply(item)
        self.assertEqual(tamagotchi.stats["food"], 100)
        self.assertEqual(tamagotchi.stats["happiness"], 100)
        self.assertEqual(tamagotchi.stats["hygiene"], 100)
        self.assertEqual(tamagotchi.stats["health"], 100)
        self.assertEqual(tamagotchi.stats["energy"], 100)
        self.assertEqual(tamagotchi.stats["age"], 0)

    def test_apply_reduces(self):
        tamagotchi = Tamagotchi()
        item = Item(-10, 0, 0, 0, 0, 0)
        tamagotchi.apply(item)
        self.assertEqual(tamagotchi.stats["food"], 90)
        self.assertEqual(tamagotchi.stats["happiness"], 100)
        self.assertEqual(tamagotchi.stats["hygiene"], 100)
        self.assertEqual(tamagotchi.stats["health"], 100)
        self.assertEqual(tamagotchi.stats["energy"], 100)
        self.assertEqual(tamagotchi.stats["age"], 0)

    def test_apply_below_zero(self):
        tamagotchi = Tamagotchi()
        item = Item(-101, 0, 0, 0, 0, 0)
        tamagotchi.apply(item)
        self.assertEqual(tamagotchi.stats["food"], 0)
        self.assertEqual(tamagotchi.stats["happiness"], 100)
        self.assertEqual(tamagotchi.stats["hygiene"], 100)
        self.assertEqual(tamagotchi.stats["health"], 100)
        self.assertEqual(tamagotchi.stats["energy"], 100)
        self.assertEqual(tamagotchi.stats["age"], 0)

    def test_second_pass_awake_half(self):
        tamagotchi = Tamagotchi()
        tamagotchi.second_pass(4*3600)
        self.assertEqual(tamagotchi.stats["energy"], 50)
        self.assertEqual(tamagotchi.stats["hygiene"], 50)
        self.assertEqual(tamagotchi.stats["food"], 0)
        self.assertEqual(tamagotchi.stats["happiness"], 0)

    def test_second_pass_awake_full(self):
        tamagotchi = Tamagotchi()
        tamagotchi.second_pass(8*3600)
        self.assertEqual(tamagotchi.stats["energy"], 0)
        self.assertEqual(tamagotchi.stats["hygiene"], 0)
        self.assertEqual(tamagotchi.stats["food"], 0)
        self.assertEqual(tamagotchi.stats["happiness"], 0)

    def test_second_pass_asleep(self):
        tamagotchi = Tamagotchi()
        tamagotchi.energy = 0
        tamagotchi.is_sleeping = True
        tamagotchi.second_pass(8*3600)
        self.assertEqual(tamagotchi.stats["energy"], 100)
        self.assertEqual(tamagotchi.stats["hygiene"], 0)
        self.assertEqual(tamagotchi.stats["food"], 0)
        self.assertEqual(tamagotchi.stats["happiness"], 0)

if __name__ == '__main__':
    unittest.main()

import unittest

from src.compare import *
# from src.compare import colour_of_apple

class TestCompare(unittest.TestCase):
    def setup (self):
        self.twin_1 = ("Jenny", 30, 5.5)
        self.twin_2 = ("Claire", 30, 5.6)

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare_numbers(3, 1))
        
    # def test_compare_height(self):
    #     self.assertEqual("Claire is taller than Jenny", self.compare_height(self.twin_1, self.twin_2))


    def test_colour_of_apple(self):
        self.assertEqual("The apple is red", colour_of_apple("red"))

    def test_distance_travelled(self):
        self.assertEqual("Andrew travelled further than John", distance_travelled("Andrew", "John"))

    # def test_add_grapes_to_list(self):
    #     shopping_list = shopping_list[]
    #     self.assertEqual(shopping_list["grapes"], add_grapes_to_list("grapes"))
import unittest
import pymunk

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.space = pymunk.Space()
        self.rect_1 = Rectangle(space=self.space, center_pos=(10,10), size=15, mass=2)

    def test_resize(self):
        self.rect_1.resize(2)
        self.assertEqual(self.rect_1.size, 30)
        self.assertEqual(self.rect_1.mass, 8)

    def test_move2pos(self):
        _pos = (150,200)
        self.rect_1.move2pos(_pos)
        self.assertEqual(self.rect_1.center_pos, _pos)

    def test_draw(self):
        self.assertTrue(self.rect_1.draw())


if __name__ == '__main__':
    unittest.main()
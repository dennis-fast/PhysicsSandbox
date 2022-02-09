import unittest
import pymunk

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.space = pymunk.Space()
        self.tria_1 = Triangle(self.space, (10,10), size = 30, mass = 2)

    def test_resize(self):
        self.tria_1.resize(2)
        self.assertEqual(self.tria_1.radius, 30)

    def test_move2pos(self):
        _pos = (150,200)
        self.tria_1.move2pos(_pos)
        self.assertEqual(self.tria_1.center_pos, _pos)

    def test_draw(self):
        self.assertTrue(self.tria_1.draw())


if __name__ == '__main__':
    unittest.main()
import unittest
import pymunk

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from circle import Circle

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.space = pymunk.Space()
        self.circle_1 = Circle(self.space, (10,10))

    def test_resize(self):
        self.circle_1.resize(2)
        self.assertEqual(self.circle_1.radius, 30)

    def test_move2pos(self):
        _pos = (150,200)
        self.circle_1.move2pos(_pos)
        self.assertEqual(self.circle_1.center_pos, _pos)

    def test_draw(self):
        self.assertTrue(self.circle_1.draw())


if __name__ == '__main__':
    unittest.main()
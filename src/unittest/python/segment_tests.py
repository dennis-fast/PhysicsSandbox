import unittest
import pymunk

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from physics_engine.segment import Segment

class TestSegment(unittest.TestCase):

    def setUp(self):
        self.space = pymunk.Space()
        self.seg_1 = Segment(space=self.space, pos_start=(0,0), pos_end=(100,100), elasticity = 0.9)

    def test_reset_elasticity(self):
        self.seg_1.reset_elasticity()
        self.assertEqual(self.seg_1.elasticity, 0.5)

    def test_draw(self):
        self.assertTrue(self.seg_1.draw())


if __name__ == '__main__':
    unittest.main()
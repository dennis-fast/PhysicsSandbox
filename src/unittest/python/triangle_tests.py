import unittest
import pymunk

from physics_engine.triangle import Triangle


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.space = pymunk.Space()
        self.tria_1 = Triangle(self.space, (10,10), size = 30, mass = 2)

    def test_move2pos(self):
        _pos = (150,200)
        self.tria_1.move2pos(_pos)
        self.assertEqual(self.tria_1.center_pos, _pos)

    def test_draw(self):
        self.assertTrue(self.tria_1.draw())


if __name__ == '__main__':
    unittest.main()
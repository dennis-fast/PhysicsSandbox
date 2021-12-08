import pymunk
from physics_engine.segment import Segment

class Box:
    def __init__(self, space, p0=(0, 50), p1=(800, 600), d=4):
        self.space = space
        x0, y0 = p0
        x1, y1 = p1
        ps = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            Segment(space, ps[i], ps[(i+1) % 4], d)
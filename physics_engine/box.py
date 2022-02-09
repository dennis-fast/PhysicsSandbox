import pymunk
from physics_engine.segment import Segment

class Box:
    def __init__(self,
                 space,
                 left_bottom_corner=(0,50),
                 right_upper_corner=(800,600),
                 line_thickness=4):
        self.space = space
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.ps = [(self.pos_start[0], self.pos_start[1]),
                   (self.pos_end[0], self.pos_start[1]),
                   (self.pos_end[0], self.pos_end[1]),
                   (self.pos_start[0], self.pos_end[1])]

        for i in range(4):
            Segment(space=space,
                    pos_start=self.ps[i],
                    pos_end=self.ps[(i+1) % 4],
                    line_thickness=line_thickness)
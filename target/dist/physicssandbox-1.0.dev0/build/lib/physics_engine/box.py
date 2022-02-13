from .segment import Segment


class Box:
    def __init__(self,
                 space,
                 left_bottom_corner=(0, 50),
                 right_upper_corner=(800, 600),
                 line_thickness=4):
        self.space = space
        self.pos_start = left_bottom_corner
        self.pos_end = right_upper_corner
        self.edge_coordinates = [(self.pos_start[0], self.pos_start[1]),
                                 (self.pos_end[0], self.pos_start[1]),
                                 (self.pos_end[0], self.pos_end[1]),
                                 (self.pos_start[0], self.pos_end[1])]

        self.center_pos = [(self.pos_start[0] + self.pos_end[0]) / 2,
                           (self.pos_start[1] + self.pos_end[1]) / 2]

        self.line_thickness = line_thickness

    def draw(self) -> bool:
        for i in range(4):
            Segment(space=self.space,
                    pos_start=self.edge_coordinates[i],
                    pos_end=self.edge_coordinates[(i + 1) % 4],
                    line_thickness=self.line_thickness)
        return True

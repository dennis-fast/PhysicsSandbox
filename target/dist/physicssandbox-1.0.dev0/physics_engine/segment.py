import pymunk


class Segment:
    def __init__(self,
                 space: pymunk.Space,
                 pos_start: (float, float),
                 pos_end: (float, float),
                 line_thickness: float = 4.,
                 color: (int, int, int) = (255, 255, 255),
                 density: float = 0.1,
                 elasticity: float = 0.5,
                 friction: float = 0.9):
        self.space = space
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.thickness = line_thickness
        self.color = color
        self.density = density
        self.elasticity = elasticity
        self.friction = friction

        self.shape = pymunk.Segment(body=self.space.static_body,
                                    a=self.pos_start,
                                    b=self.pos_end,
                                    radius=self.thickness)

        self.shape.density = self.density
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

    def reset_elasticity(self) -> bool:
        self.elasticity = 0.5
        return True

    def draw(self) -> bool:
        self.space.add(self.shape)
        return True

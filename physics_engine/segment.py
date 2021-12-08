import pymunk

class Segment():
    def __init__(self, _space: pymunk.Space, _pos_start: (int, int), _pos_end: (int, int), _thickness: float = 4, _color: (int, int, int) = (255, 255, 255), _density: float = 0.1 , _elasticity: float = 0.5, _friction: float = 0.9):

        self.space = _space
        self.pos_start = _pos_start
        self.pos_end = _pos_end
        self.thickness = _thickness
        
        self.density = _density
        self.elasticity = _elasticity
        self.friction = _friction

        self.shape = pymunk.Segment(self.space.static_body, self.pos_start, self.pos_end, self.thickness) 

        self.color = _color

        self.shape.density = self.density
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

        self.space.add(self.shape)
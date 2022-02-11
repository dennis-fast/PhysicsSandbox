import pymunk

import math


class Triangle:
    def __init__(self,
                 space: pymunk.Space,
                 center_pos: (float, float),
                 size: float = 20,
                 mass: float = 1,
                 friction: float = 0.5,
                 elasticity: float = 0.5):
        self.space = space
        self.center_pos = center_pos
        self.size = size
        self.mass = mass
        self.friction = friction
        self.elasticity = elasticity

        self.vertices = self.set_vertices(self.size)

        self.shape = pymunk.Poly(body=None,
                                 vertices=self.vertices)

        self.moment = pymunk.moment_for_poly(mass=self.mass,
                                             vertices=self.shape.get_vertices())

        self.body = pymunk.Body(mass=self.mass,
                                moment=self.moment,
                                body_type=pymunk.Body.DYNAMIC)

        self.body.position = self.center_pos

        self.shape.body = self.body
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

    def set_vertices(self, _size: float) -> (float, float, float):
        _vertex_1 = (-_size / 2, -_size / 6 * math.sqrt(3))
        _vertex_2 = (_size / 2, -_size / 6 * math.sqrt(3))
        _vertex_3 = (0, _size / 3 * math.sqrt(3))
        return (_vertex_1, _vertex_2, _vertex_3)

    def move2pos(self, _pos: (float, float)) -> bool:
        self.center_pos = _pos
        return True

    def draw(self) -> bool:
        self.space.add(self.body, self.shape)
        return True

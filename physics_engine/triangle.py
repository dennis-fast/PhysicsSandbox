import pymunk

import math

class Triangle():
    def __init__(self, _space: pymunk.Space, _x: int, _y: int, _size: int = 20, _mass: int = 1, _friction: float = 0.5, _elasticity: float = 0.5):
        self.space = _space
        self.x = _x
        self.y = _y
        self.size = _size
        self.mass = _mass
        self.friction = _friction
        self.elasticity = _elasticity

        self.__vertex_1 = (-self.size/2, -(self.size/6)*math.sqrt(3))
        self.__vertex_2 = (self.size/2, -(self.size/6)*math.sqrt(3))
        self.__vertex_3 = (0, (self.size/3)*math.sqrt(3))

        self.shape = pymunk.Poly(None, (self.__vertex_1, self.__vertex_2, self.__vertex_3))
        self.moment = pymunk.moment_for_poly(self.mass, self.shape.get_vertices())
        self.body = pymunk.Body(self.mass, self.moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = (self.x, self.y)
        self.shape.body = self.body

        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

        self.draw()

    def draw(self):
        self.space.add(self.body, self.shape)
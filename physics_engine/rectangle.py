import pymunk

class Rectangle():
    def __init__(self, _space: pymunk.Space, _x: int, _y: int, _size: int = 20, _mass: int = 1, _friction: float = 0.5, _elasticity: float = 0.5):
        self.space = _space
        self.x = _x
        self.y = _y
        self.size = _size
        self.mass = _mass
        self.friction = _friction
        self.elasticity = _elasticity

        self.shape = pymunk.Poly.create_box(None, size=(self.size,self.size))
        self.moment = pymunk.moment_for_poly(self.mass, self.shape.get_vertices())
        self.body = pymunk.Body(self.mass, self.moment, body_type=pymunk.Body.DYNAMIC)
        self.body.position = (self.x, self.y)
        self.shape.body = self.body

        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

        self.draw()

    def draw(self):
        self.space.add(self.body, self.shape)
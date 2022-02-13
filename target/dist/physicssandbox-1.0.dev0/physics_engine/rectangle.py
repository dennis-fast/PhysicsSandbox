import pymunk


class Rectangle():
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

        self.shape = pymunk.Poly.create_box(body=None,
                                            size=(self.size, self.size))

        self.moment = pymunk.moment_for_poly(mass=self.mass,
                                             vertices=self.shape.get_vertices())

        self.body = pymunk.Body(mass=self.mass,
                                moment=self.moment,
                                body_type=pymunk.Body.DYNAMIC)

        self.body.position = self.center_pos
        self.shape.body = self.body

        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

    def move2pos(self, _pos: (float, float)) -> bool:
        self.center_pos = _pos
        return True

    def draw(self) -> bool:
        self.space.add(self.body, self.shape)
        return True

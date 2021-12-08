import pymunk

class Circle():
    def __init__(self, _space: pymunk.Space, _x: int, _y: int, _radius: float = 15., _body_type: str = 'dynamic', _color: (int, int, int) = (0, 255, 0), _density: float = 0.01 , _elasticity: float = 1., _friction: float = 0.9):

        self.space = _space
        self.x = _x
        self.y = _y
        self.radius = _radius
        self.body_type = _body_type
        self.color = _color
        self.density = _density
        self.elasticity = _elasticity
        self.friction = _friction

        self.body = pymunk.Body()

        if self.body_type == 'static':
            self.body.body_type = pymunk.Body.STATIC
            #print(self.body_type)
        elif self.body_type == 'kinematic':
            self.body.body_type = pymunk.Body.KINEMATIC
            #print(self.body_type)
        else:
            self.body.body_type = pymunk.Body.DYNAMIC
            #print(self.body_type)

        self.body.position = (self.x, self.y)

        self.shape = pymunk.Circle(self.body, self.radius)

        self.shape.density = self.density
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

        self.space.add(self.body, self.shape)

        def draw():
            pygame.draw.circle()
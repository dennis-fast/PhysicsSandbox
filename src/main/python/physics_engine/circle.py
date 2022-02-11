import pymunk


class Circle:
    def __init__(self,
                 space: pymunk.Space,
                 center_pos: (float, float),
                 radius: float = 15.,
                 body_type: str = 'dynamic',
                 color: (int, int, int) = (0, 255, 0),
                 density: float = 0.01,
                 elasticity: float = 1.,
                 friction: float = 0.9):

        self.space = space
        self.center_pos = center_pos
        self.radius = radius
        self.body_type = body_type
        self.color = color
        self.density = density
        self.elasticity = elasticity
        self.friction = friction

        self.body = pymunk.Body()

        if self.body_type == 'static':
            self.body.body_type = pymunk.Body.STATIC
        elif self.body_type == 'kinematic':
            self.body.body_type = pymunk.Body.KINEMATIC
        else:
            self.body.body_type = pymunk.Body.DYNAMIC

        self.body.position = self.center_pos

        self.shape = pymunk.Circle(body=self.body,
                                   radius=self.radius)

        self.shape.density = self.density
        self.shape.elasticity = self.elasticity
        self.shape.friction = self.friction

    def move2pos(self, _pos: (float, float)) -> bool:
        self.center_pos = _pos
        return True

    def draw(self) -> bool:
        self.space.add(self.body, self.shape)
        return True

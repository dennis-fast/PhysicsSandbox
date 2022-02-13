import pyglet
from pyglet.window import mouse
from pyglet.window import key
import pymunk
from pymunk.pyglet_util import DrawOptions

import physics_engine as pe

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


class Sandbox(pyglet.window.Window):
    def __init__(self):
        super(Sandbox, self).__init__(width=SCREEN_WIDTH,
                                      height=SCREEN_HEIGHT,
                                      caption="Physics Sandbox",
                                      resizable=False,
                                      fullscreen=False)

        self.options = pymunk.pyglet_util.DrawOptions()

        self.set_mouse_visible(True)
        self.cursor_pos = [0, 0]
        self.keys_pressed = {}

        # updates screen every 1/120 seconds -> 500 FPS
        self.fps = 120
        pyglet.clock.schedule_interval(func=self.update, interval=1/self.fps)

        self.space = pymunk.Space()
        self.space.gravity = (0, -981/2)
        self.elasticity = 0.9
        self.friction = 0.9

        self.ground = pe.Segment(space=self.space,
                                 pos_start=(0, 100),
                                 pos_end=(SCREEN_WIDTH, 10),
                                 line_thickness=10,
                                 elasticity=self.elasticity,
                                 friction=self.friction).draw()

    # update screen
    def update(self, _dt: float) -> None:
        self.on_draw()
        self.space.step(_dt)

        # delete shapes which are outside of the screen
        for _shape in self.space.shapes:
            if _shape.body.position.y < -100:
                self.space.remove(_shape.body, _shape)

    # ------------------------------------------------------------------------
    # event handlers
    def on_draw(self) -> None:
        self.clear()
        self.space.debug_draw(self.options)
       
    def on_mouse_motion(self, _x: int, _y: int, _dx: int, _dy: int) -> None:
        self.cursor_pos[0] += _dx
        self.cursor_pos[1] += _dy

    def on_mouse_press(self, _x: int, _y: int,
                       _button: int, _modifiers: int) -> None:
        if _button == mouse.LEFT:
            print("Left mouse button pressed -> generate a rectangle")
            rec = pe.Rectangle(self.space, self.cursor_pos)
            rec.draw()
            
            # self.on_mouse_motion(_x, _y, _dx, _dy)

        if _button == mouse.RIGHT:
            print("Right mouse button pressed -> generate a circle")
            pe.Circle(space=self.space, center_pos=self.cursor_pos).draw()
            # self.on_mouse_motion(_x, _y, _dx, _dy)

    def on_key_press(self, _symbol: int, _modifiers: int) -> None:
        self.keys_pressed[_symbol] = True

        if _symbol == key.SPACE and self.keys_pressed[_symbol] == True:
            print("The SPACE BAR was pressed -> generate a triangle")
            tri = pe.Triangle(space=self.space, center_pos=self.cursor_pos)
            tri.draw()

    def on_key_release(self, _symbol: int, _modifiers: int) -> None:
        del self.keys_pressed[_symbol]

    # ------------------------------------------------------------------------

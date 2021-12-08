import pyglet
from pyglet.window import mouse
from pyglet.window import key
import pymunk
from pymunk.pyglet_util import DrawOptions

import physics_engine as pe

SCREEN_WIDTH  = 1280
SCREEN_HEIGHT = 720

class Sandbox(pyglet.window.Window):
    def __init__(self):
        super(Sandbox, self).__init__(SCREEN_WIDTH, SCREEN_HEIGHT, resizable=False, fullscreen=False, caption="Physics Sandbox")
        self.options = pymunk.pyglet_util.DrawOptions()
        #self.batch = pyglet.graphics.Batch()

        self.set_mouse_visible(True)

        # cursor position
        self.mouse_pos = [0,0]

        self.keys = {}

        pyglet.clock.schedule_interval(func=self.update, interval=1.0/120) # 500 FPS

        self.space = pymunk.Space()
        self.space.gravity = (0, -981/2)
        self.elasticity = 0.9
        self.friction = 0.9

        self.floor = pe.Segment(self.space, (0, 100), (SCREEN_WIDTH, 10), 10)
        #self.floor.id = 1
        self.floor.elasticity = self.elasticity
        self.floor.friction = self.friction
        #self.space.add(self.floor)

        #radius = 30
        #mass = 1

        #self.sprites = []

        # --------------------------------------------------------------------------------------------------------------    
        # Collision handler
        def coll_begin(arbiter, space, data):
            #print(arbiter.shapes)
            return True

        def coll_pre(arbiter, space, data):
            return True
    
        def coll_post(arbiter, space, data):
            pass
    
        def coll_separate(arbiter, space, data):
            pass

        self.handler = self.space.add_default_collision_handler()
        self.handler.begin = coll_begin
        self.handler.pre_solve = coll_pre
        self.handler.post_solve = coll_post
        self.handler.separate = coll_separate
        # --------------------------------------------------------------------------------------------------------------   

    # update screen
    def update(self,dt):
        self.on_draw()
        self.space.step(dt)

        # delete shapes which are outside of the screen
        for shape in self.space.shapes:
            if shape.body.position.y < -100:
                self.space.remove(shape.body, shape)
                # print(self.space.shapes)

    # --------------------------------------------------------------------------------------------------------------
    # event handlers
    def on_draw(self):
        self.clear()
        self.space.debug_draw(self.options)
        #self.smile_sprite.draw()
        #self.batch.draw()
        #self.cursor.blit(self.mouse_pos[0],self.mouse_pos[1])
        #self.fps_display.draw()
       
    def on_mouse_motion(self,x,y,dx,dy):
        self.mouse_pos[0] += dx
        self.mouse_pos[1] += dy
        #print(self.mouse)

    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        self.mouse_pos[0] += dx
        self.mouse_pos[1] += dy

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            print ("The left mouse button was pressed -> generate a rectangle")
            pe.Rectangle(self.space, x, y)

        if button == mouse.RIGHT:
            print ("The right mouse button was pressed -> generate a circle")
            pe.Circle(self.space, x, y)

    def on_key_press(self, symbol, modifiers):
        self.keys[symbol] = True

        if symbol == key.SPACE and self.keys[symbol] == True:
            print ("The SPACEBAR was pressed -> generate a triangle")
            pe.Triangle(self.space, self.mouse_pos[0], self.mouse_pos[1])

    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
            #print(self.keys)
        except:
            pass
    # --------------------------------------------------------------------------------------------------------------
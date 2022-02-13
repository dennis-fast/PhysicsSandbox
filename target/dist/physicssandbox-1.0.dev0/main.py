import pyglet

from sandbox import Sandbox

if __name__ == '__main__':
    try:
        s = Sandbox()
        pyglet.app.run()
    finally:
        s.close()

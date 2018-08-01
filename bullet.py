from object import Object

class Bullet(Object):
    def __init__(self, x, y, vel ):
        Object.__init__(self, x, y, 5, 5, (0,255,0), vel)

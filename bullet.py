from person import Person

class Bullet(Person):
    def __init__(self, x, y, vel ):
        Person.__init__(self, x, y, 5, 5, (0,255,0), vel)

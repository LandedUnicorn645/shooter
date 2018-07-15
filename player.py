from person import Person

class Player(Person):
    def __init__(self, x, y, width, height,  vel, color ):
        Person.__init__(self, x, y, width, height, color, vel)

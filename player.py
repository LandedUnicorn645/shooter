from person import Person
from gun import Gun

class Player(Person):
    def __init__(self, x, y, width, height,  vel, color ):
        Person.__init__(self, x, y, width, height, color, vel)
        self._gun = Gun()

    def __getGun(self):
        return self._gun

    gun = property(__getGun)

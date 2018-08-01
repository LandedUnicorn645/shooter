from object import Object

class Person(Object):
    def __init__(self, x, y, width, height, color, vel, health, shields):
        Object.__init__(self, x, y, width, height, color, vel,)
        self._health = health
        self._shields = shields
        if self._shields:
            self._shieldper = 100
        else:
            self._shieldper = 0

    def __getHealth(self):
        return self._health

    def __setHealth(self, newhealth):
        self._health = newhealth

    def __getShields(self):
        return self._shieldper

    def __setShields(self, percent):
        self._shieldper = percent
        if self._shieldsper <= 0:
            self._shields = False

    def __hasShields(self):
        return self._shields

    health = property(__getHealth, __setHealth)
    shields = property(__getShields, __setShields)
    hasshields = property(__hasShields)

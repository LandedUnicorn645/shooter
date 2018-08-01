import random
from person import Person

class Enemy(Person):
    def __init__(self, width, height, screenwidth, screenheight, vel, type):
        self._isalive = True
        self._type = type
        if self._type == 1:
            color = (255,0,0)
            health = 50
            shields = False
            False
        elif self._type == 2:
            color = (255,20,147)
            health = 75
            shields = False
        elif self._type == 3:
            color = (0,128,128)
            health = 50
            shields = True
        Person.__init__(self, random.randint(5, screenwidth),random.randint(5, screenheight), width, height,color, vel, health, shields)

    def __getStatus(self):
        return self._isalive

    def __setStatus(self, status):
        self._isalive = status

    alive = property(__getStatus, __setStatus)

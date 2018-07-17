import random
from person import Person

class Enemy(Person):
    def __init__(self, width, height, screenwidth, screenheight, vel):
        Person.__init__(self, random.randint(5, screenwidth),random.randint(5, screenheight), width, height,(255,0,0), vel)
        self._isalive = True

    def __getStatus(self):
        return self._isalive

    def __setStatus(self, status):
        self._isalive = status

    alive = property(__getStatus, __setStatus) 

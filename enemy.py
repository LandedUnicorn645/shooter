import random
from person import Person

class Enemy(Person):
    def __init__(self, width, height, screenwidth, screenheight, vel):
        Person.__init__(self, random.randint(5, screenwidth),random.randint(5, screenheight), width, height,(255,0,0), vel)

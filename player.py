from person import Person
from machinegun import MachineGun

class Player(Person):
    def __init__(self, x, y, width, height,  vel, color):
        Person.__init__(self, x, y, width, height, color, vel, 100, False)
        self.mgun = MachineGun(30)
        self.weapons = {"Gun":[self.mgun]}
        self.inventory = {"weapons": self.weapons}
        self.currweapon = self.mgun
        self.shootdir = 'left'
        self.lastdir = 'left'

    def __getWeapon(self):
        return self.currweapon

    weapon = property(__getWeapon)

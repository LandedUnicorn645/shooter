from person import Person
from machinegun import MachineGun

class Player(Person):
    def __init__(self, x, y, width, height,  vel, color ):
        Person.__init__(self, x, y, width, height, color, vel, 100, False)
        self._mgun = MachineGun(30)
        self._weapons = {"Gun":[self._mgun]}
        self._inventory = {"weapons": self._weapons}

        self._currweapon = self._mgun


    def __getWeapon(self):
        return self._currweapon

    weapon = property(__getWeapon)

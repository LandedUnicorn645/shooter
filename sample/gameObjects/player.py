from gameObjects.person import Person
from gameObjects.weapons import MachineGun
from gameObjects.bullet import Bullet

class Player(Person):
    def __init__(self, x, y, width, height,  vel, color, settings):
        Person.__init__(self, x, y, width, height, color, vel, 100, False)
        self.mgun = MachineGun(30)
        self.weapons = {"Gun":[self.mgun]}
        self.inventory = {"weapons": self.weapons}
        self.currweapon = self.mgun
        self.shootdir = 'left'
        self.lastdir = 'left'
        self.settings = settings

    def __getWeapon(self):
        return self.currweapon

    def _shoot(self):
        self.currweapon.bul += 1
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        if self.shootdir == 'right':
            bulletx = x + width
            bullety = y + (height//4)

        elif self.shootdir == 'left':
            bulletx = x - 5
            bullety = y + (height//2)

        elif self.shootdir == "up":
            bulletx = x + (width//2)
            bullety = y - 5

        elif self.shootdir == 'down':
            bulletx = x + (width//2)
            bullety = y + height

        if self.shootdir == self.lastdir:
            vel = self.vel + 2
        else:
            vel = 5
        bullet = Bullet(bulletx, bullety, vel)
        self.weapon.addBullet(bullet)
        self.settings.objectlist.append(bullet)
        self.settings.bulletlist.append((bullet,self.shootdir))


    weapon = property(__getWeapon)

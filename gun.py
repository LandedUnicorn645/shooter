
class Gun:
    def __init__(self, maxammo=30, lockon=False):
        self._maxammo = maxammo
        self._totalbul = 0
        self._lock = lockon
        self._bullets = []

    def __getAmmo(self):
        return self._maxammo

    def __setAmmo(self, ammo):
        self._maxmmo = ammo

    def __getBul(self):
        return self._totalbul

    def __setBul(self, bul):
        self._totalbul = bul

    def __getLock(self):
        return self._lock

    def __setLock(self, lock):
        self._lock = lock

    def __getbullets(self):
        return self._bullets

    def __setBullets(self, bullet):
        self._bullets = []

    def addBullet(self, bullet):
        if self._totalbul < self._maxammo:
            self._bullets.append(bullet)
        else:
            return
    bul = property(__getBul, __setBul)
    ammo = property( __getAmmo, __setAmmo)
    lock = property( __getLock, __setLock)
    bullet = property( __getbullets)

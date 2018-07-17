import pygame
from player import Player
from enemy import Enemy

class Game:
    pygame.init()
    #make it full screen
    def __init__(self):
        self._SCREENWIDTH = 1000
        self._SCREENHEIGHT = 1000
        self._win = pygame.display.set_mode((self._SCREENWIDTH,self._SCREENHEIGHT))
        self._running = True
        #self._lastdirection = 'right'
        #self._newdirection = 'left'
        self._player = Player(500, 500, 20, 20, 10, (0,0,255))
        self._enemydict = {}
        self._enemylist = []
        self._enemynum = 5
        self._lvl = 1
        self._dead = 0

    def run(self):
        self._enemynum += self._lvl
        self.createEnemies()
        while self._running:
            x = self._player.x
            y = self._player.y
            vel = self._player.vel
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and x > 0:

                x -= vel
                self._player.x = x
            if keys[pygame.K_RIGHT] and x < self._SCREENWIDTH - 20:

                x += vel
                self._player.x = x
            if keys[pygame.K_DOWN] and y < self._SCREENHEIGHT - 20:

                y += vel
                self._player.y = y
            if keys[pygame.K_UP] and y > 0:
                y -= vel
                self._player.y = y

            self._win.fill((0,0,0))
            pygame.draw.rect(self._win, self._player.color, (self._player.x, self._player.y, self._player.width, self._player.height))
            self.drawEnemy()
            self.moveEnemy()
            pygame.display.update()
        pygame.quit()

    def createEnemies(self):
        for e in range(self._enemynum):
            enemy = Enemy(10,10,self._SCREENWIDTH,self._SCREENHEIGHT, 1)
            self._enemylist.append(enemy)


    def drawEnemy(self):
        for e in self._enemylist:
            if e.alive:
                print("Enemy : ", e.x," ", e.y )
                pygame.draw.rect(self._win, e.color, (e.x, e.y, e.width, e.height))
            else:
                continue

    def moveEnemy(self):
        x = self._player.x
        y = self._player.y
        for e in self._enemylist:
            if e.alive:
                if e.x == x  and  e.y == y:
                    self.collision(e)
                else:
                    self._checkX(e, x)
                    self._checkY(e, y)
            else:
                continue

    def collision(self, e):
        e.alive = False
        print("Changing status")
        return e

    def _checkX(self, enemy, value):
        if enemy.x > value:
            enemy.x -= enemy.vel
        elif enemy.x < value:
            enemy.x += enemy.vel

    def _checkY(self, enemy, value):
        if enemy.y >= value:
            enemy.y -= enemy.vel
        elif enemy.y <= value:
            enemy.y += enemy.vel

if __name__ == "__main__":
    game = Game()
    game.run()

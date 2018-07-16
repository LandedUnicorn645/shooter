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

            if keys[pygame.K_LEFT]:

                x -= vel
                self._player.x = x
            if keys[pygame.K_RIGHT]:

                x += vel
                self._player.x = x
            if keys[pygame.K_DOWN]:

                y += vel
                self._player.y = y
            if keys[pygame.K_UP]:

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
            enemy = Enemy(10,10,self._SCREENWIDTH,self._SCREENHEIGHT, 10)
            self._enemylist.append(enemy)


    def drawEnemy(self):
        for e in self._enemylist:
            pygame.draw.rect(self._win, e.color, (e.x, e.y, e.width, e.height))

    def moveEnemy(self):
        x = self._player.x
        y = self._player.y
        for e in self._enemylist:
            self._checkX(e, x)
            self._checkY(e, y)

    def _checkX(self, enemy, value):
        if enemy.x > value:
            enemy.x -= enemy.vel
        elif enemy.x < value:
            enemy.x += enemy.vel
        else:
            enemy.color = (0,0,0)

    def _checkY(self, enemy, value):
        if enemy.y > value:
            enemy.y -= enemy.vel
        elif enemy.y < value:
            enemy.y += enemy.vel
        else:
            enemy.color = (0,0,0)

if __name__ == "__main__":
    game = Game()
    game.run()

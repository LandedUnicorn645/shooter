import pygame, copy, time
from player import Player
from enemy import Enemy
from bullet import Bullet

class Game:
    '''A Game class that runs the game and monitors the state of the game from what level
        to the number of enemies

        '''
    pygame.init()
    #make it full screen
    def __init__(self):
        self._SCREENWIDTH = 1000
        self._SCREENHEIGHT = 1000
        self._win = pygame.display.set_mode((self._SCREENWIDTH,self._SCREENHEIGHT))
        self._running = True
        self._shootdir = 'left'
        self._player = Player(500, 500, 20, 20, 10, (0,0,255))
        self._objectlist = []
        self._bulletdirection = {'up': [], 'down': [], 'left': [], 'right':[]}
        self._enemylist = []
        self._enemynum = 5
        self._lvl = 0
        self._dead = 0

    def run(self):
        while True:
            self._enemynum += self._lvl
            self._objectlist.append(self._player)
            self._createEnemies()
            self._lvl += 1
            text = "lvl " + str(self._lvl)
            self.message_display(text)
            self._win.fill((0,0,0))
            while len(self._enemylist) > 0:
                x = self._player.x
                y = self._player.y
                vel = self._player.vel
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a] and x > 0:
                    self._lastdir = 'left'
                    x -= vel
                    self._player.x = x
                if keys[pygame.K_d] and x < self._SCREENWIDTH - 20:
                    self._lastdir = 'right'
                    x += vel
                    self._player.x = x
                if keys[pygame.K_s] and y < self._SCREENHEIGHT - 20:
                    self._lastdir = 'down'
                    y += vel
                    self._player.y = y

                if keys[pygame.K_w] and y > 0:
                    self._lastdir = 'up'
                    y -= vel
                    self._player.y = y

                if keys[pygame.K_SPACE]:
                    if keys[pygame.K_LEFT]:
                        self._shootdir = 'left'
                    if keys[pygame.K_RIGHT]:
                        self._shootdir = 'right'
                    if keys[pygame.K_DOWN]:
                        self._shootdir = 'down'
                    if keys[pygame.K_UP]:
                        self._shootdir = 'up'
                    self._shoot()

                self._win.fill((0,0,0))
                self._draw()
                pygame.display.update()
                self._moveEnemy()
                self._moveBullet()

        pygame.quit()

    def message_display(self,text):
        textype = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.text_objects(text, textype)
        TextRect.center = ((self._SCREENWIDTH/2),(self._SCREENHEIGHT/2))
        pygame.display.set_mode((self._SCREENWIDTH, self._SCREENHEIGHT)).blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def text_objects(self,text, font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

    def _draw(self):
        for object in self._objectlist:
            pygame.draw.rect(self._win, object.color, (object.x, object.y, object.width, object.height))

    def _createEnemies(self):
        for e in range(self._enemynum + 1):
            enemy = Enemy(10,10,self._SCREENWIDTH,self._SCREENHEIGHT, 1)
            self._enemylist.append(enemy)
            self._objectlist.append(enemy)

    def _moveEnemy(self):
        x = self._player.x
        y = self._player.y
        for e in list(self._enemylist):
            if e.x == x  and  e.y == y:
                self._collision()
            else:
                self._checkX(e, x)
                self._checkY(e, y)

    def _shoot(self):
        x = self._player.x
        y = self._player.y
        width = self._player.width
        height = self._player.height
        if self._shootdir == 'right':
            bulletx = x + width
            bullety = y + (height//4)
            bullet = Bullet(bulletx, bullety, 5)

        elif self._shootdir == 'left':
            bulletx = x - 5
            bullety = y + (height//2)
            bullet = Bullet(bulletx, bullety, 5)

        elif self._shootdir == "up":
            bulletx = x + (width//2)
            bullety = y - 5
            bullet = Bullet(bulletx, bullety, 5)

        elif self._shootdir == 'down':
            bulletx = x + (width//2)
            bullety = y + height
            bullet = Bullet(bulletx, bullety, 5)
        self._bulletdirection[self._shootdir].append(bullet)
        self._objectlist.append(bullet)


    def _moveBullet(self):
        dirkey = self._bulletdirection.keys()
        for key in dirkey:
            for bul in self._bulletdirection[key]:
                if key == 'up':
                    bul.y -= bul.vel
                elif key == 'down':
                    bul.y += bul.vel
                elif key == 'right':
                    bul.x += bul.vel
                elif key == 'left':
                    bul.x = bul.x - bul.vel
        self._checkHit()

    def _checkHit(self):
        dirkey = self._bulletdirection.keys()
        for key in dirkey:
            for bul in list(self._bulletdirection[key]):
                bulx = bul.x
                buly = bul.y
                bulw = bul.width
                bulh = bul.height
                for enemy in list(self._enemylist):
                    ex = enemy.x
                    ey = enemy.y
                    ew = enemy.width
                    eh = enemy.height
                    if bulx + bulw >= ex and bulx + bulw <= ex + ew:
                        if buly + bulh >= ey and buly + bulh <= ey + eh:
                            enemy.color = (255,255,255)
                            self._hit(enemy)


    def _hit(self, e):
        self._enemylist.remove(e)
        self._objectlist.remove(e)

    def _collision(self):
        self._lvl = 0
        self._enemylist = []
        self._objectlist = []
        keys = self._bulletdirection.keys()
        for key in keys:
            self._bulletdirection[key] = []
        self.message_display("Game Over!")

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

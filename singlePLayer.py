import pygame, copy, time, random
from player import Player
from enemy import Enemy
from bullet import Bullet

class SinglePLayerGame:
    '''A Game class that runs the game and monitors the state of the game from what level
        to the number of enemies

        '''
    pygame.init()
    def __init__(self):
        self._SCREENWIDTH = 1000
        self._SCREENHEIGHT = 1000
        self._win = pygame.display.set_mode((self._SCREENWIDTH,self._SCREENHEIGHT))
        self._shootdir = 'left'
        self._lastdir = 'left'
        self._player = Player(500, 500, 20, 20, 10, (0,0,255))
        self._objectlist = []
        self._bulletlist = []
        self._enemylist = []
        self._score = 0
        self._enemynum = 5
        self._lvl = 10

    def run(self):
        self._message_display("Start")
        while True:
            self._enemynum += self._lvl
            self._player.weapon.bul = 0
            self._lvl += 1
            self._win.fill((0,0,0))
            text = "lvl " + str(self._lvl)
            self._message_display(text)
            self._bulletlist = []
            self._objectlist = []
            self._objectlist.append(self._player)
            self._createEnemies()
            while len(self._enemylist) > 0:

                x = self._player.x
                y = self._player.y
                vel = self._player.vel
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

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
                    if self._player.weapon.bul < self._player.weapon.ammo:
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
                self._scoreCal()
                pygame.display.update()
                self._moveEnemy()
                self._moveBullet()

    def _message_display(self,text):
        textype = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self._text_objects(text, textype)
        TextRect.center = ((self._SCREENWIDTH/2),(self._SCREENHEIGHT/2))
        self._win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def _text_objects(self,text, font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

    def _scoreCal(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("score: "+str(self._score)+" "+"Bullets : "+str(self._player.weapon.bul)+"/30", True, (255,255,255))

        self._win.blit(text, (0,0))

    def _draw(self):
        for object in self._objectlist:
            pygame.draw.rect(self._win, object.color, (object.x, object.y, object.width, object.height))

    def _createEnemies(self):
        for e in range(self._enemynum + 1):
            if self._lvl > 3:
                type = random.randint(1,2)
            elif self._lvl > 10:
                type = randim.ranint(1,3)
            else:
                type = 1
            print("type : ", type)
            enemy = Enemy(10,10,self._SCREENWIDTH,self._SCREENHEIGHT, 3, type)
            self._enemylist.append(enemy)
            self._objectlist.append(enemy)

    def _moveEnemy(self):
        x = self._player.x
        y = self._player.y
        w = self._player.width
        h = self._player.height
        for e in list(self._enemylist):
            if e.x + e.width >= x  and e.x  <= x + w:
                if e.y + e.height >= y and e.y  <= y + h:

                    self._collision()
                else:
                    self._checkY(e, y)
            else:
                self._checkX(e, x)
                self._checkY(e, y)

    def _shoot(self):
        self._player.weapon.bul += 1
        x = self._player.x
        y = self._player.y
        width = self._player.width
        height = self._player.height
        if self._shootdir == 'right':
            bulletx = x + width
            bullety = y + (height//4)

        elif self._shootdir == 'left':
            bulletx = x - 5
            bullety = y + (height//2)

        elif self._shootdir == "up":
            bulletx = x + (width//2)
            bullety = y - 5

        elif self._shootdir == 'down':
            bulletx = x + (width//2)
            bullety = y + height

        if self._shootdir == self._lastdir:
            vel = self._player.vel + 2
        else:
            vel = 5
        bullet = Bullet(bulletx, bullety, vel)
        self._player.weapon.addBullet(bullet)
        self._objectlist.append(bullet)
        self._bulletlist.append((bullet,self._shootdir))

    def _moveBullet(self):
        for pair in list(self._bulletlist):
            bul = pair[0]
            key = pair[1]
            remove = False
            if key == 'up':
                if bul.y > 0:
                    bul.y -= bul.vel
                else:
                    remove = True
            elif key == 'down':
                if bul.y < self._SCREENHEIGHT:
                    bul.y += bul.vel
                else:
                    remove = True
            elif key == 'right':
                if bul.x < self._SCREENWIDTH:
                    bul.x += bul.vel
                else:
                    remove = True
            elif key == 'left':
                if bul.x > 0:
                    bul.x = bul.x - bul.vel
                else:
                    remove = True
            if remove:
                self._bulletlist.remove(pair)
                self._objectlist.remove(bul)
                self._player.weapon.bul -= 1
        for bul in self._bulletlist:
            print(bul)
        self._checkHit()

    def _checkHit(self):
        print()
        for pair in list(self._bulletlist):
            bul = pair[0]
            bulx = bul.x
            buly = bul.y
            bulw = bul.width
            bulh = bul.height
            for enemy in list(self._enemylist):
                ex = enemy.x
                ey = enemy.y
                ew = enemy.width
                eh = enemy.height
                if bulx + bulw >= ex and bulx <= ex + ew:
                    if buly + bulh >= ey and buly  <= ey + eh:
                        self._hit(enemy, pair)
                        break

    def _hit(self, e, tup):
        if e.hasshields:
            e.shields -= 25
        else:
            e.health -= 30
            if e.health <= 0:
                self._enemylist.remove(e)
                self._objectlist.remove(e)
                self._score += 50
        self._bulletlist.remove(tup)
        self._objectlist.remove(tup[0])
        self._player.weapon.bul -= 1

    def _collision(self):
        if self._player.hasshields:
            self._player.shields -= 30
        else:
            self._player.health -= 50
            if self._player.health == 0:
                self._message_display("Game Over!")
                self._lvl = 0
                self._enemylist = []
                self._objectlist = []


    def _checkX(self, enemy, value):
        if enemy.x > value:
            enemy.x -= enemy.vel
        elif enemy.x < value:
            enemy.x += enemy.vel

    def _checkY(self, enemy, value):
        if enemy.y > value:
            enemy.y -= enemy.vel
        elif enemy.y < value:
            enemy.y += enemy.vel

if __name__ == "__main__":
    game = Game()
    game.run()

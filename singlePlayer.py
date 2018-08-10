import pygame, copy, time, random
from player import Player
from enemy import Enemy
from bullet import Bullet


class SinglePLayerGame:
    '''A Game class that runs the game and monitors the state of the game from what level
        to the number of enemies

        '''
    pygame.init()
    def __init__(self, settings):
        self.settings = settings
        self.win = self.settings.win
        self.player = Player(500, 500, 20, 20, 10, (0,0,255), self.settings)

    def run(self):
        self.win.fill((0,0,0))
        self._message_display("Start")
        while True:
            self.settings.set(self.player)
            text = "lvl " + str(self.settings.lvl)
            self._message_display(text)
            self._createEnemies()
            while len(self.settings.enemylist) > 0:
                x = self.player.x
                y = self.player.y
                vel = self.player.vel
                pygame.time.delay(100)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a] and x > 0:
                    self.player.lastdir = 'left'
                    x -= vel
                    self.player.x = x

                if keys[pygame.K_d] and x < self.settings.screenwidth - 20:
                    self.player.lastdir = 'right'
                    x += vel
                    self.player.x = x

                if keys[pygame.K_s] and y < self.settings.screenheight - 20:
                    self.player.lastdir = 'down'
                    y += vel
                    self.player.y = y

                if keys[pygame.K_w] and y > 0:
                    self.player.lastdir = 'up'
                    y -= vel
                    self.player.y = y

                if keys[pygame.K_SPACE]:
                    if self.player.weapon.bul < self.player.weapon.ammo:
                        if keys[pygame.K_LEFT]:
                            self.player.shootdir = 'left'

                        elif keys[pygame.K_RIGHT]:
                            self.player.shootdir = 'right'

                        elif keys[pygame.K_DOWN]:
                            self.player.shootdir = 'down'

                        elif keys[pygame.K_UP]:
                            self.player.shootdir = 'up'

                        self.player._shoot()

                self.win.fill((0,0,0))
                self._draw()
                self._scoreCal()
                pygame.display.update()
                self._moveEnemy()
                self._moveBullet()

    def _message_display(self,text):
        textype = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self._text_objects(text, textype)
        TextRect.center = ((self.settings.screenwidth/2),(self.settings.screenheight/2))
        self.win.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def _text_objects(self,text, font):
        textSurface = font.render(text,True,(255,255,255))
        return textSurface, textSurface.get_rect()

    def _scoreCal(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("score: "+str(self.settings.score)+" "+"Bullets : "+str(self.player.weapon.bul)+"/30", True, (255,255,255))
        self.settings.win.blit(text, (0,0))


    def _draw(self):
        for object in self.settings.objectlist:
            pygame.draw.rect(self.win, object.color, (object.x, object.y, object.width, object.height))

    def _createEnemies(self):
            if self.settings.lvl > 3 and self.settings.lvl < 10:
                for e in range(self.settings.enemynum + 1):
                    type = random.randint(1,2)
                    enemy = Enemy(10,10,self.settings.screenwidth,self.settigs.screenheight, 3, type)
                    self.settings.enemylist.append(enemy)
                    self.settings.objectlist.append(enemy)
            elif self.settings.lvl > 10:
                for e in range(self.settings.enemynum//2):
                    type = random.ranint(2,3)
                    enemy = Enemy(10,10,self.settings.screenwidth,self.settigs.screenheight, 3, type)
                    self.settings.enemylist.append(enemy)
                    self.settings.objectlist.append(enemy)
            else:
                for e in range(self.settings.enemynum+1):
                    type = 1
                    enemy = Enemy(10,10,self.settings.screenwidth,self.settings.screenheight, 3, type)
                    self.settings.enemylist.append(enemy)
                    self.settings.objectlist.append(enemy)

    def _moveEnemy(self):
        x = self.player.x
        y = self.player.y
        w = self.player.width
        h = self.player.height
        for e in list(self.settings.enemylist):
            if e.x + e.width >= x  and e.x  <= x + w:
                if e.y + e.height >= y and e.y  <= y + h:

                    self._collision()
                else:
                    self._checkY(e, y)
            else:
                self._checkX(e, x)
                self._checkY(e, y)

    def _moveBullet(self):
        for pair in list(self.settings.bulletlist):
            bul = pair[0]
            key = pair[1]
            remove = False
            if key == 'up':
                if bul.y > 0:
                    bul.y -= bul.vel
                else:
                    remove = True
            elif key == 'down':
                if bul.y < self.settings.screenheight:
                    bul.y += bul.vel
                else:
                    remove = True
            elif key == 'right':
                if bul.x < self.settings.screenwidth:
                    bul.x += bul.vel
                else:
                    remove = True
            elif key == 'left':
                if bul.x > 0:
                    bul.x = bul.x - bul.vel
                else:
                    remove = True
            if remove:
                self.settings.bulletlist.remove(pair)
                self.settings.objectlist.remove(bul)
                self.player.weapon.bul -= 1
        self._checkHit()

    def _checkHit(self):
        for pair in list(self.settings.bulletlist):
            bul = pair[0]
            bulx = bul.x
            buly = bul.y
            bulw = bul.width
            bulh = bul.height
            for enemy in list(self.settings.enemylist):
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
                self.settings.enemylist.remove(e)
                self.settings.objectlist.remove(e)
                self.settings.score += 50
        self.settings.bulletlist.remove(tup)
        self.settings.objectlist.remove(tup[0])
        self.player.weapon.bul -= 1

    def _collision(self):
        if self.player.hasshields:
            self.player.shields -= 30
        else:
            self.player.health -= 50
            if self.player.health == 0:
                self._message_display("Game Over!")
                self.settings.lvl = 0
                self.settings.enemylist = []
                self.settings.objectlist = []
                self.player.weapon.bul = 0
                self.settings.score = 0

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
    game = SinglePLayerGame()
    game.run()

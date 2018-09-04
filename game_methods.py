import pygame, time
from enemy import Enemy

def _createEnemies(settings, color):
        print("settings.enemynum : ",settings.enemynum)
        if settings.lvl > 3 and settings.lvl < 10:
            for e in range(settings.enemynum + 1):
                if color == (0,0,255):
                    ecolor = (255,0,0)
                elif color == (255,0,0):
                    ecolor = (0,0,255)
                type = random.randint(1,2)
                enemy = Enemy(10,10,settings.screenwidth,settings.screenheight, 3, type, ecolor)
                settings.enemylist.append(enemy)
                settings.objectlist.append(enemy)
        elif settings.lvl > 10:
            for e in range(settings.enemynum//2):
                type = random.ranint(2,3)
                enemy = Enemy(10,10,settings.screenwidth,settings.screenheight, 3, type)
                settings.enemylist.append(enemy)
                settings.objectlist.append(enemy)
        else:
            for e in range(settings.enemynum+1):
                type = 1
                enemy = Enemy(10,10,settings.screenwidth,settings.screenheight, 3, type)
                settings.enemylist.append(enemy)
                settings.objectlist.append(enemy)

def _message_display(settings, text):
    textype = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = _text_objects(text, textype)
    TextRect.center = ((settings.screenwidth/2),(settings.screenheight/2))
    settings.win.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def _text_objects(text, font):
    textSurface = font.render(text,True,(255,255,255))
    return textSurface, textSurface.get_rect()

def _moveEnemy(settings):
    x = settings.player.x
    y = settings.player.y
    w = settings.player.width
    h = settings.player.height
    for e in list(settings.enemylist):
        if e.x + e.width >= x  and e.x  <= x + w:
            if e.y + e.height >= y and e.y  <= y + h:
                _collision(settings, e)
            else:
                _checkY( e, y)
        else:
            _checkX( e, x)
            _checkY(e, y)

def _moveBullet(settings):
    for pair in list(settings.bulletlist):
        bul = pair[0]
        key = pair[1]
        remove = False
        if key == 'up':
            if bul.y > 0:
                bul.y -= bul.vel
            else:
                remove = True
        elif key == 'down':
            if bul.y < settings.screenheight:
                bul.y += bul.vel
            else:
                remove = True
        elif key == 'right':
            if bul.x < settings.screenwidth:
                bul.x += bul.vel
            else:
                remove = True
        elif key == 'left':
            if bul.x > 0:
                bul.x = bul.x - bul.vel
            else:
                remove = True
        if remove:
            settings.bulletlist.remove(pair)
            settings.objectlist.remove(bul)
            settings.player.weapon.bul -= 1
    _checkHit(settings)

def _checkHit(settings):
    for pair in list(settings.bulletlist):
        bul = pair[0]
        bulx = bul.x
        buly = bul.y
        bulw = bul.width
        bulh = bul.height
        for enemy in list(settings.enemylist):
            ex = enemy.x
            ey = enemy.y
            ew = enemy.width
            eh = enemy.height
            if bulx + bulw >= ex and bulx <= ex + ew:
                if buly + bulh >= ey and buly  <= ey + eh:
                    _hit(settings, enemy, pair)
                    break

def _hit(settings, e, tup):
    if e.hasshields:
        e.shields -= 25
    else:
        e.health -= 30
        if e.health <= 0:
            settings.enemylist.remove(e)
            settings.objectlist.remove(e)
            settings.score += 50
    settings.bulletlist.remove(tup)
    settings.objectlist.remove(tup[0])
    settings.player.weapon.bul -= 1

def _collision(settings, e):
    settings.enemylist.remove(e)
    settings.objectlist.remove(e)
    if settings.player.hasshields:
        settings.player.shields -= 30
    else:
        settings.player.health -= 50
        if settings.player.health == 0:)
            _message_display(settings, "Game Over!")
            settings.lvl = 0
            settings.enemylist = []
            settings.objectlist = []
            settings.player.weapon.bul = 0
            settings.score = 0
            settings.enemynum = 4
            settings.player.health = 100


def _checkX( enemy, value):
    if enemy.x > value:
        enemy.x -= enemy.vel
    elif enemy.x < value:
        enemy.x += enemy.vel

def _checkY( enemy, value):
    if enemy.y > value:
        enemy.y -= enemy.vel
    elif enemy.y < value:
        enemy.y += enemy.vel

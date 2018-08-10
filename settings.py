import pygame
class Settings:
    def __init__(self, tup, window):
        self.screenheight = tup[1]
        self.screenwidth = tup[0]
        self.state = "main"
        self.win = window
        self.score = 0
        self.lvl = 0
        self.objectlist = []
        self.bulletlist = []
        self.enemylist = []
        self.enemynum = 4

    def set(self, player):
        self.objectlist = []
        self.bulletlist = []
        self.enemylist = []
        self.enemynum += 2
        self.addPlayer(player)
        self.lvl += 1
        self.win.fill((0,0,0))

    def addPlayer(self, player):
        self.objectlist.append(player)

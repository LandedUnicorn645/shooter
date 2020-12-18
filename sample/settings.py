class Settings:
    '''Settings object that will keep information baout hte current game

        Parameters :
            tup - the current width and height of the window respectfully
            window - the window the game is running on

        Attributes :
            screenheight - the heoght of the screen
            screenwidth - the width of the screen
            state - the state of the game, 'main' is main menu
            score - the players current score in the game
            lvl - the level the player is on
            objectlist - the list of objects that need to be drawn(bullst, enemies, player,etc)
            bulletlist - the list of bullets fired (max 30)
            enemylist - the list of enemies that are alive
            enemynum - he number of enemies (changes for each level)

    '''
    def __init__(self, tup, window):
        self.screenheight = tup[1]
        self.screenwidth = tup[0]
        self.state = "main"
        self.win = window
        self.score = 0
        self.lvl = 0
        self.player = None
        self.objectlist = []
        self.bulletlist = []
        self.enemylist = []
        self.enemynum = 4

    def set(self, player):
        self.player = player
        self.objectlist = []
        self.bulletlist = []
        self.enemylist = []
        self.enemynum += 2
        self.addPlayer(player)
        self.lvl += 1
        self.win.fill((0,0,0))

    def addPlayer(self, player):
        self.objectlist.append(player)

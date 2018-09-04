import pygame
from singlePlayer import SinglePLayerGame

class Menu:
    """ A menu object that changes the options depending obn the state of the game

        Parameters :
            settings - settings objects that holds the state of the game and window

        Attributes :

            settings - points to the settings object
            menuoptions - list of options in the menu available to the user
            prevstate - the previous state the game was.
                        used for 'Return button in menu'(used as a stack )
            win - window everything gets drawn on
            pointer - the menu option the user is at/pointing to
            background_image - the background image for the menu

    """
    def __init__(self, settings):
        self.settings = settings
        self.menuoptions = []
        self.prevstate = []
        self.win = self.settings.win
        self.pointer = 0
        self.background_image = pygame.image.load("game_image.jpg")#.convert()
        self.setMenuOptions()


    def draw(self):
        self.win.blit(self.background_image, (0,0))
        for item in self.menuoptions:
            item.draw(self.win)

    def setMenuOptions(self):
        self.menuoptions = []
        if self.settings.state == "main":
           'add the appropriate menu options in here'
           opt1 = Opt("Start",self.settings.screenwidth/2,self.settings.screenheight/4 , 0 )
           opt2 = Opt("Settings",self.settings.screenwidth/2,self.settings.screenheight/2, 1 )
           opt3 = Opt("Quit", self.settings.screenwidth/2,(self.settings.screenheight/4)*3, 2 )

        elif self.settings.state == "pause":
           opt1 = Opt("Return",self.settings.screenwidth/2,self.settings.screenheight/4,0 )
           opt2 = Opt("Settings",self.settings.screenwidth/2,self.settings.screenheight/2,1 )
           opt3 = Opt("Quit", self.settings.screenwidth/2,(self.settings.screenheight/4)*3,2)
        elif self.settings.state == "settings":
           opt1 = Opt("Controls", self.settings.screenwidth/2,self.settings.screenheight/4,0)
           opt2 = Opt("player", self.settings.screenwidth/2,self.settings.screenheight/2, 1)
           opt3 = Opt("Return", self.settings.screenwidth/2,(self.settings.screenheight/4)*3, 2)
        elif self.settings.state == "controls":
           opt1 = Opt("w,s,a,d : move player", self.settings.screenwidth/2,self.settings.screenheight/4,1, 30)
           opt2 = Opt("spacebar : shoot", self.settings.screenwidth/2, (self.settings.screenheight/20)*7, 2, 30)
           opt3 = Opt("arrow keys : change shooting direction", self.settings.screenwidth/2,(self.settings.screenheight/20)*9, 3, 30)
           opt4 = Opt("Return", self.settings.screenwidth/2, (self.settings.screenheight/20)*17,0  )
           self.pointer = 0
           self.menuoptions.append(opt4)

        self.menuoptions.append(opt1)
        self.menuoptions.append(opt2)
        self.menuoptions.append(opt3)
        self.menuoptions[self.pointer].select = True

    def increasePointer(self):
        print("increasing")
        self.menuoptions[self.pointer].select = False
        if self.pointer == 0:
            self.pointer = len(self.menuoptions)-1
        else:
            self.pointer -= 1
        self.menuoptions[self.pointer].select = True

    def decreasePointer(self):
        print("decreasing")
        self.menuoptions[self.pointer].select = False
        if self.pointer == len(self.menuoptions)-1:
            self.pointer = 0
        else:
            self.pointer += 1
        self.menuoptions[self.pointer].select = True

    def mouse_motion(self, event):
        for item in self.menuoptions:
            item.mouse_hover(event)
            if item.select:
                self.pointer = item.pos

    def activated_Option(self):
        text = self.menuoptions[self.pointer].text
        if text == "Quit":
            pygame.quit()
            quit()
        else:
            if text == "Start":
                game = SinglePLayerGame(self.settings)
                game.run()
                '''self.prevstate.append(self.settings.state)
                self.settings.state = "game"'''
            elif text == "S1inglePlayer":
                game = SinglePLayerGame(self.settings)
                game.run()
            elif text == "Controls":
                self.prevstate.append(self.settings.state)
                self.settings.state = "controls"
            elif text == "Settings":
                self.prevstate.append(self.settings.state)
                self.settings.state = "settings"
            elif text == "Return":
                self.settings.state = self.prevstate[len(self.prevstate)-1]
                self.prevstate.pop()
            self.setMenuOptions()
class Opt:
    def __init__(self, text, x, y, pos, size = 100):
        self.select = False
        self.text = text
        self.x = x
        self.y = y
        self.font = "freesansbold.ttf"
        self.size = size
        self.color = (255,255,255)
        self.rect = None
        self.pos = pos

    def draw(self, screen):
        textype = pygame.font.Font(self.font, self.size)
        if self.select:
            self.color = (0,0,255)
        else:
            self.color = (255,255,255)
        text = textype.render(self.text, 0, self.color)
        self.rect = text.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(text, self.rect)

    def mouse_hover(self, event):
        mouseX = event.pos[0]
        mouseY = event.pos[1]
        if self.rect:
            if mouseX > self.rect.x and mouseX < self.rect.x + self.rect.width:
                if mouseY > self.rect.y and mouseY < self.rect.y + self.rect.height:
                    self.select = True
                    return
        self.select = False

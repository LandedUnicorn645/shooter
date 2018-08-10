import pygame
from singlePlayer import SinglePLayerGame

class Menu:
    def __init__(self, settings):
        self.settings = settings
        self.menuoptions = []
        self.prevstate = []
        self.win = self.settings.win
        self.pointer = 0
        self.setMenuOptions()


    def draw(self):
        for item in self.menuoptions:
            item.draw(self.win)

    def setMenuOptions(self):
        self.menuoptions = []
        if self.settings.state == "main":
           'add the appropriate menu options in here'
           opt1 = Opt("Start",500, 250, 0 )
           opt2 = Opt("Settings",500,500, 1 )
           opt3 = Opt("Quit", 500,750, 2 )
        elif self.settings.state == "pause":
           opt1 = Opt("Return",500,250,0 )
           opt2 = Opt("Settings",500,500,1 )
           opt3 = Opt("Quit", 500,750,2)
        elif self.settings.state == "settings":
           opt1 = Opt("Controls", 500,250,0)
           opt2 = Opt("player", 500, 500, 1)
           opt3 = Opt("Return", 500,750, 2)
        elif self.settings.state == "controls":
           opt1 = Opt("w,s,a,d : move player", 500,250,1, 30)
           opt2 = Opt("spacebar : shoot", 500, 350, 2, 30)
           opt3 = Opt("arrow keys : change shooting direction", 500,450, 3, 30)
           opt4 = Opt("Return", 500, 850,0  )
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
        print(self.pointer)
        text = self.menuoptions[self.pointer].text
        print(self.menuoptions[self.pointer].text)
        if text == "Start":
            game = SinglePLayerGame(self.settings)
            game.run()
        elif text == "Controls":
            self.prevstate.append(self.settings.state)
            self.settings.state = "controls"
            self.setMenuOptions()

        elif text == "Settings":
            self.prevstate.append(self.settings.state)
            self.settings.state = "settings"
            self.setMenuOptions()
        elif text == "Return":
            print("Enter")
            self.settings.state = self.prevstate[len(self.prevstate)-1]
            self.prevstate.pop()
            self.setMenuOptions()
        elif text == "Quit":
            pygame.quit()
            quit()

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

        # Creates a new Font Object with that font style and size
        textype = pygame.font.Font(self.font, self.size)
        # Draws self._text to a new Surface
        if self.select:
            self.color = (0,0,255)
        else:
            self.color = (255,255,255)
        text = textype.render(self.text, 0, self.color)
        # Gets the rectangle for the text
        self.rect = text.get_rect()
        # Gives the rectangle it s center (not the top left corner)

        self.rect.center = (self.x, self.y)
        screen.blit(text, self.rect)

    def mouse_hover(self, event):
        mouseX = event.pos[0]
        mouseY = event.pos[1]
        if mouseX > self.rect.x and mouseX < self.rect.x + self.rect.width:
            if mouseY > self.rect.y and mouseY < self.rect.y + self.rect.height:
                self.select = True
                return
        self.select = False

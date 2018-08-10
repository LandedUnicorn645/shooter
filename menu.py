import pygame
from singlePlayer import SinglePLayerGame

class Menu:
    def __init__(self, settings):
        self.settings = settings
        self.menuoptions = []
        self.win = self.settings.win
        self.pointer = 0
        self.setMenuOptions()


    def draw(self):
        for item in self.menuoptions:
            item.draw(self.win)

    def setMenuOptions(self):

        if self.settings.state == "main":
           'add the appropriate menu options in here'
           opt1 = Opt("Start",500, 250, 0 )
           self.menuoptions.append(opt1)
           opt2 = Opt("Settings",500,500, 1 )
           self.menuoptions.append(opt2)
           opt3 = Opt("Quit", 500,750, 2 )
           self.menuoptions.append(opt3)
        elif self.settings.state == "pause":
           opt1 = Opt("Return", )
           self.menuoptions.append(opt1)
           opt2 = Opt("Settings", )
           self.menuoptions.append(opt2)
           opt3 = Opt("Quit", )
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
        if text == "Start":
            game = SinglePLayerGame(self.settings)
            game.run()
        elif text == "Settings":
            'display settings'
        elif text == "Quit":
            pygame.quit()
            quit()

class Opt:
    def __init__(self, text, x, y, pos):
        self.select = False
        self.text = text
        self.x = x
        self.y = y
        self.font = "freesansbold.ttf"
        self.size = 100
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

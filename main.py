import pygame
from settings import Settings
from singlePlayer import SinglePLayerGame
from menu import Menu

def main():
    pygame.init()
    print("creating window")
    win = pygame.display.set_mode((1000,1000))
    print("creating settings")
    settings = Settings((1000,1000), win)
    menu = Menu(settings)
    menu.draw()
    while True:
        pygame.time.delay(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                menu.mouse_motion(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                menu.activated_Option()
        if settings.state != "controls":

            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN]:
                print("DOWN")
                menu.decreasePointer()

            elif keys[pygame.K_UP]:
                print("UP")
                menu.increasePointer()

            elif keys[pygame.K_RIGHT]:
                menu.activated_Option()

        win.fill((0,0,0))
        menu.draw()
        pygame.display.update()

if __name__ == "__main__":
    print("calling main()")
    main()

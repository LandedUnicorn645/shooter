import pygame, random

def game():
    pygame.init()
    #make it full screen
    win = pygame.display.set_mode((1000,1000))
    #pygame.display.set_caption()
    running = True
    player = createPlayer()
    x = player[0]
    y = player[1]
    height = player[2]
    width = player[3]
    vel = player[4]
    color = player[5]
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_DOWN]:
            y += vel
        if keys[pygame.K_UP]:
            y -= vel


        win.fill((0,0,0))
        pygame.draw.rect(win, color, (x,y,width,height))
        pygame.display.update()
    pygame.quit()
def createPlayer():
    player = [500, 500, 40, 40, 10, (0,0,255)]
    return player

if __name__ == "__main__":
    game()

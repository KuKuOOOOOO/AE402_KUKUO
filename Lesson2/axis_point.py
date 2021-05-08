
import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
PINK = pygame.color.Color("#FF87EE")
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("畫出一個圓心")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, 250), (700, 250), 4)
    pygame.draw.line(screen, BLACK, (350,0), (350, 500), 4)
    pygame.draw.circle(screen,BLACK,(100,50),2,2)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()


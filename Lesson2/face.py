import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("我的遊戲")

done = False

clock = pygame.time.Clock()


while not done:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    screen.fill(WHITE)
    
    pygame.draw.circle(screen, BLACK, (150,150), 130, 4)
    pygame.draw.circle(screen, BLUE, (100,120), 25, 0)
    pygame.draw.circle(screen, BLUE, (200,120), 25, 0)
    pygame.draw.ellipse(screen, GREEN,[135, 130, 30, 80], 0)
    pygame.draw.arc(screen, RED, [80, 130, 150, 120], 3.14, 6.28, 9)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()


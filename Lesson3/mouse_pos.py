import pygame
 
WHITE = (255, 255, 255)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("滑鼠")
 
done = False

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
 
    screen.fill(WHITE)
 
    pygame.display.flip()

    clock.tick(60)
pygame.quit()

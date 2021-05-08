""" 
遞迴方塊
"""
import pygame
 
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
 
def recursive_draw(x, y, width, height):
    pygame.draw.rect(screen, black, 
                     [x,y,width,height],
                     1)

    if( width > 14 ):
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        recursive_draw(x, y, width, height)
    
pygame.init()
  
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True
 
    screen.fill(white)
 
    recursive_draw(0, 0, 700, 500)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

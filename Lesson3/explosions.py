import pygame
import random

def randColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
BLACK = (0, 0, 0)
pygame.init()
size = (400, 300)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

color = randColor()
count = 0
click = False #控制判斷是否點擊
limit = 30 #圓要爆炸的大小

while not done:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            click = True
            count = 0
            color = randColor()
    if click and count < limit:
        pygame.draw.circle(screen, color, pos, count)
        count += 1
        if count >= limit:
            click = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
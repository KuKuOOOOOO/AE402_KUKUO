
import pygame, random
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("下雪動畫")

# 雪的座標
x = random.randrange(0, 400)
y = random.randrange(0, 400)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # 畫圓形代表雪
    pygame.draw.circle(screen, WHITE, (x,y), 30)
    # y每次加1，雪往下飄落
    y = y + 1
    # 當雪掉到地面......
    if y > 400:
        #調到底之後重新從上面掉
        y = 0
        # 給一個隨機的x位置
        x = random.randrange(0, 400)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


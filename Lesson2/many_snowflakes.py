import pygame, random

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

#size = (400, 400)
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("下雪動畫")

# 創造空的list，儲存雪的座標
snow_list = []
# 產生50個雪花
for i in range(50):
    # 雪的座標
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    screen.fill(BLACK)

    
    for i in range(len(snow_list)):
        # 畫圓形代表雪
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # y每次加1，雪往下飄落
        snow_list[i][1] += 1
    
        # 當雪掉到地面......
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = 0
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x
        
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


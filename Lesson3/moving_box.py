import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

size = (400, 300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("走動的方塊")

done = False

clock = pygame.time.Clock()


# -------- 主要的程式迴圈 -----------
# 方塊初始位置
x = 0
y = 0

while not done:
    # --- 事件迴圈 event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x, y, 10, 10])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1                
    elif keys[pygame.K_RIGHT]:
        x += 1
    elif keys[pygame.K_UP]:
        y -= 1
    elif keys[pygame.K_DOWN]:
        y += 1
    else:
        pass    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


"""
碰撞 -- 一對一
"""
import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# player的初始位置
player_x = 0
player_y = 0
player_w = 50
player_h = 50
# block的初始位置
block_w = 50
block_h = 50
block_x = random.randrange(screen_width-block_w)
block_y = random.randrange(screen_height-block_h)
# 判斷有無撞到的布林變數
collision = False
# 分數
score = 0
# font物件
font = pygame.font.Font(None, 50)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        
    # 清除視窗畫面
    screen.fill(WHITE)

    # 取得滑鼠座標 (list of (x,y))
    pos = pygame.mouse.get_pos()
    # 畫出player & block
    player_x = pos[0] - 25
    player_y = pos[1] - 25
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    if not collision:
        pygame.draw.rect(screen, BLACK, [block_x, block_y, block_w, block_h])
        
    # 判斷是否碰撞到了
    xin = block_x <= player_x <= block_x+block_w or block_x <= player_x+player_w <= block_x+block_w
    yin = block_y <= player_y <= block_y+block_h or block_y <= player_y+player_h <= block_y+block_h
    if  xin and yin and not collision:
        collision = True
        score += 1

    # 顯示分數
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    
    # 新畫面更新
    pygame.display.flip()

    # 一秒60個frame
    clock.tick(60)

pygame.quit()

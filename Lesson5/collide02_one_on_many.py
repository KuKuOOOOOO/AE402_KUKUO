"""
碰撞 -- 一對一
"""
import pygame
import random

# 顏色常數
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

# 初始化pygame
pygame.init()

# 設定設窗大小
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# player的初始位置
player_x = 0
player_y = 0
player_w = 50
player_h = 50
# block的初始化
block_x = []
block_y = []
collisions = []
for i in range(10):
    # Set a random location for the block
    block_x.append(random.randrange(screen_width))
    block_y.append(random.randrange(screen_height))
    collisions.append(False)
  
block_w = 50
block_h = 50
score = 0
font = pygame.font.Font(None, 50)
FinishGame = 0
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks() #starter tick

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    # Clear the screen
    screen.fill(WHITE)
    
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000) #calculate how many seconds
   
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()        
        
    # 畫出player & block          
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen, RED, [player_x, player_y, player_w, player_h])
    for i in range(10):
        if not collisions[i]:
            pygame.draw.rect(screen, BLACK, [block_x[i], block_y[i], block_w, block_h])
    
    # 判斷是否碰撞到了
    for i in range(10):
        xin = block_x[i]<=player_x<=block_x[i]+block_w or block_x[i]<=player_x+player_w<=block_x[i]+block_w
        yin = block_y[i]<=player_y<=block_y[i]+block_h or block_y[i]<=player_y+player_h<=block_y[i]+block_h
        if  xin and yin and not collisions[i]:
            collisions[i] = True
            score += 1

    # 顯示分數
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))

    for i in range(10):
        if collisions[i] == True:
            FinishGame = FinishGame + 1
    # 顯示時間
    t = font.render(str(seconds), 10, RED)
    screen.blit(t, (40,40))
    
    if seconds>10:
        text = font.render("GAME OVER", 10, BLACK)
        screen.blit(text, (100,100))
        done=True
    
    if FinishGame == 10:
        text1 = font.render("Finish", 0, BLACK)
        screen.blit(text1, (300, 200))
    else:
        FinishGame = 0
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(144)

pygame.quit()

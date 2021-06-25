"""
 貪食蛇-->加上蘋果與音效、分數
"""

import pygame
import random
from queue import Queue

# --- Globals ---
# 顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# 貪食蛇每個segment的寬與高
segment_width = 48
segment_height = 48
# 每個segment間的間隙
segment_margin = 2
# 目前貪食蛇頭的座標
segment_head_x = 0
segment_head_y = 0

# 設定初始速度
x_change = 1
y_change = 0

score = 0
# Segment類別
class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- 方法
    # 建構式
    def __init__(self, x, y):
        # 呼叫父建構式
        super().__init__()

        # 設定寬與高
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # 左上角座標
        self.rect = self.image.get_rect()
        self.rect.x = x*(segment_width+segment_margin)
        self.rect.y = y*(segment_height+segment_margin)
        
        self.x = x
        self.y = y

# 初始化pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode([800, 600])

# 視窗標題
pygame.display.set_caption('貪食蛇')

# 所有角色的group物件
allspriteslist = pygame.sprite.Group()

# 創造初始的貪食蛇
snake_segments = Queue()
for i in range(5):
    x = 3 + i
    y = 3
    segment = Segment(x, y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y
    print(i, segment.x, segment.y)
clock = pygame.time.Clock()
done = False
eat = True
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 1

     
    # 創造最新的一個segment
    segment_head_x += x_change
    segment_head_y += y_change
    segment = Segment(segment_head_x, segment_head_y)

    # 將新的segment插入list中的第一位
    snake_segments.put(segment)
    allspriteslist.add(segment)

    # apple
    if eat:
        xa = random.randrange(16)
        ya = random.randrange(12)
        eat = False
    else:# 拿掉貪食蛇的最後一個segment  # 利用list的pop() # 如果吃到蘋果就不pop-->加長
        old_segment = snake_segments.get()
        allspriteslist.remove(old_segment)
    apple = Segment(xa,ya)
    
    # Determine if the snake eats the apple   
    if segment.x==apple.x and segment.y==apple.y:
        score = score+1
        pygame.display.set_caption("貪食蛇|分數: "+ str(score))
        eat = True
    # -- 畫出所有東西
    # Clear screen
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, (xa*(segment_width+segment_margin),ya*(segment_width+segment_margin),segment_width,segment_height))
    allspriteslist.draw(screen)
    
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

pygame.quit()
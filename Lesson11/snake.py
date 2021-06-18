"""
 貪食蛇 
"""

import pygame
from queue import Queue

# --- Globals ---
# 顏色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 貪食蛇每個segment的寬與高
segment_width = 15
segment_height = 15
# 每個segment間的間隙
segment_margin = 3
segment_head_x = 0
segment_head_y = 0

# 設定初始速度
x_change = segment_width + segment_margin
y_change = 0

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
        self.rect.x = x
        self.rect.y = y

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
for i in range(15):
    x = 0 + (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.put(segment)
    allspriteslist.add(segment)
    segment_head_x = x
    segment_head_y = y


clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) *- 1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) *- 1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # 先拿掉貪食蛇的最後一個segment
    # 利用list的pop() 
    old_segment = snake_segments.get()
    allspriteslist.remove(old_segment)

    # 創造最新的一個segment
    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    segment = Segment(segment_head_x, segment_head_y)

    # 將新的segment插入list中的第一位
    snake_segments.put(segment)
    allspriteslist.add(segment)

    # -- 畫出所有東西
    # Clear screen
    screen.fill(BLACK)

    allspriteslist.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

pygame.quit()
exit()

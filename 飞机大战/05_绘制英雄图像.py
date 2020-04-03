import pygame

pygame.init()

# 确认画布
screen = pygame.display.set_mode((480, 700))

# 绘制图像
# 1.加载图像
bg = pygame.image.load('./images/background.png')

# 2.固定位置
screen.blit(source=bg, dest=(0,0))

# 3.更新显示
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150,300))
pygame.display.update()


while True:
    pass

pygame.quit()














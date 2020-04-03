import pygame

# 初始化
pygame.init()

# 创建游戏窗口 480*700
screen = pygame.display.set_mode(size=(480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load('./images/background.png')

# 2.blit绘制图像
screen.blit(source=bg, dest=(0,0))

# 3.update更新屏幕
pygame.display.update()

while True:
    pass

pygame.quit()



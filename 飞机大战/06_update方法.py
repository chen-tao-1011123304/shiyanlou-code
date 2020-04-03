import pygame

# 初始化
pygame.init()

# 创建画布
screen = pygame.display.set_mode(size=(480, 700))

# 绘制图像
# 1.放背景
bg = pygame.image.load('./images/background.png')
hero = pygame.image.load('./images/me1.png')

# 2.确认位置
screen.blit(source=bg, dest=(0,0))
screen.blit(source=hero, dest=(150,300))

# 3.更新
pygame.display.update()

while True:
    pass

# 退出
pygame.quit()




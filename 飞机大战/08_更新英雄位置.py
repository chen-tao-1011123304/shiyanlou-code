import pygame

pygame.init()

# 画布
screen = pygame.display.set_mode(size=(480, 700))

# 绘制背景图像
bg = pygame.image.load('./images/background.png')
screen.blit(source=bg, dest=(0, 0))

# 绘制英雄背景
hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150, 300))

pygame.display.update()

# 调用时钟
clock = pygame.time.Clock()

# 用rect定义飞机位置， 不用blit原因， rect可变
hero_rect = pygame.Rect(150, 300, 102, 126)


while True:
    # 60帧
    clock.tick(60)
    hero_rect.y += -1
    # 更新图像
    # 若不加 bg， 会出现黑色覆盖
    screen.blit(source=bg, dest=(0,0))
    screen.blit(source=hero, dest=hero_rect)
    pygame.display.update()


pygame.quit()
















import pygame

pygame.init()

# 创建画布
screen = pygame.display.set_mode(size=(480, 700))

# 有背景
bg = pygame.image.load('./images/background.png')
screen.blit(source=bg, dest=(0,0))

# 有英雄
hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150, 300))

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

pygame.display.update()

while True:
    # 定时器
    clock.tick(60)
    # y减一
    hero_rect.x += -1

    # 小于0 700
    if hero_rect.x < -102:
        hero_rect.x = 480

    # 更新
    screen.blit(source=bg, dest=(0, 0))
    screen.blit(source=hero, dest=hero_rect)
    pygame.display.update()

pygame.quit()
























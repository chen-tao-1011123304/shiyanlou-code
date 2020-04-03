import pygame

pygame.init()

screen = pygame.display.set_mode(size=(480, 700))

# 背景
bg = pygame.image.load('./images/background.png')
screen.blit(source=bg, dest=(0, 0))

# 英雄
hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150, 300))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)

    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
        # [ < Event(3 - KeyUp
        # {'key': 276, 'mod': 0, 'scancode': 75, 'window': None}) >]

    # 修改飞机位置
    hero_rect.x -= 1

    if hero_rect.x < -102:
        hero_rect.x = 480
    # 更新
    screen.blit(source=bg, dest=(0, 0))
    screen.blit(source=hero, dest=hero_rect)
    pygame.display.update()

pygame.quit()




























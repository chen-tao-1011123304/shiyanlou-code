import pygame

pygame.init()
# print(pygame.event.get())

screen = pygame.display.set_mode(size=(480, 700))

bg = pygame.image.load('./images/background.png')
screen.blit(source=bg, dest=(0, 0))

hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150, 300))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            # 不加表面退出
            exit()
            # break


    hero_rect.x -= 1
    if hero_rect.x == -128:
        hero_rect.x = 480

    screen.blit(source=bg, dest=(0,0))
    screen.blit(source=hero, dest=hero_rect)

    pygame.display.update()


pygame.quit()




















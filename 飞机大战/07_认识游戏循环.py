import pygame

pygame.init()

screen = pygame.display.set_mode(size=(480, 700))

bg = pygame.image.load('./images/background.png')
screen.blit(source=bg, dest=(0, 0))

hero = pygame.image.load('./images/me1.png')
screen.blit(source=hero, dest=(150, 300))

pygame.display.update()

# 创建时钟
clock = pygame.time.Clock()

i = 0

while True:
    # 频率1/10
    clock.tick(1)
    print(i)
    i += 1
    pass


pygame.quit()






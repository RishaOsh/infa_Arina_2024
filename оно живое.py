import pygame
from pygame.draw import *
from rgbhsl import intRGB
#импортирует нужные библиотеки

pygame.init()
FPS = 20
screen = pygame.display.set_mode((400, 400))
H = 0
#настраивает задержку и открывает экран

def move(x,y):
    global H
    H = (H + 1) % 360
    #rect(screen, (0, 0, 0), (0, 0, 400, 400))
    circle(screen, intRGB(H), (x,y), 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
# что-то со временем (?)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEMOTION:
            move(event.pos[0],event.pos[1])
            pygame.display.update()
        #точки которые двигаются за мышкой
        
        
#реакция на нажатия

pygame.quit()

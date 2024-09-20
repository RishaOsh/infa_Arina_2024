import pygame
from pygame.draw import *
from random import randint
from rgbhsl import intRGB
#импортирует нужные библиотеки

pygame.init()
FPS = 20
screen = pygame.display.set_mode((400, 400))

#настраивает задержку и открывает экран

H = 0
xf = 0
yf = 0 

def move(x,y):
    global H
    H = (H + 1) % 360
    #rect(screen, (0, 0, 0), (0, 0, 400, 400))
    circle(screen, intRGB(H), (x, y), 5)
    
def food(f):
    global xf,yf
    if f:
        xf = randint(0, 400)
        yf = randint(0, 400)
        circle(screen, (255,255,255), (xf, yf), 5)
    elif not(f):
        circle(screen, (0,0,0), (xf, yf), 5)
        
    
score = 0
    
food(True)

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
            if ((event.pos[0]-xf)**2 + (event.pos[1]-yf)**2) < 50:
                food(False)
                score = score + 1
                food(True)
                
            pygame.display.update()
        #точки которые двигаются за мышкой
        
print(score)       
#реакция на нажатия

pygame.quit()

from random import randint
import turtle
from math import *

#####
def color(H, n):
    L = 0.5
    S = 1
    a = S * min(L, 1-L)
    k = (n + (H/30)) % 12
    f = L - a * max(-1, min(k-3, 9-k, 1))
    return(f)
def RGB(H):
    R = color(H,0)
    G = color(H,8)
    B = color(H,4)
    return(R,G,B)
##### цвета для визуала


turtle.tracer(False)



number_of_turtles = 60
steps_of_time_number = 20000
step = 0.3

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    #unit.color(RGB(randint(0,360)))
    unit.shapesize(0.5)
    unit.speed(10)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.setheading(randint(-200, 200))
    #создаёт клонов


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(step)
        if abs(unit.pos()[0]) > 200:
            unit.backward(step)
            unit.setheading(180 - unit.heading()) 
        #Боковые границы    
            
        if abs(unit.pos()[1]) > 200:
            unit.backward(step) 
            unit.setheading(180 + unit.heading())
        #Верхиние границы
            
        for unit2 in pool:
            if unit2 != unit:
                x1 = unit.pos()[0]
                y1 = unit.pos()[1]
                x2 = unit2.pos()[0]
                y2 = unit2.pos()[1]
                if ((x1-x2)**2 + (y1-y2)**2) < 180:
                    q = unit.heading()
                    unit.setheading(unit2.heading())
                    unit2.setheading(q)
        #Отталкивение от соседей
                                   
                     
    turtle.update()
            
turtle.mainloop()
        
import turtle 

from turtle import forward, left

def rectangle():
    wide = input ('Input the wide of rectangle: ')
    wide = int (wide)
    tall = input('Input the tall of rectangle: ')
    tall = int(tall)

    forward(wide)
    left(90)

    forward(tall)
    left(90)

    forward(wide)
    left(90)

    forward(tall)
    left(90)

rectangle()
turtle.done()
    
import turtle

from turtle import left, forward

def paralelogram (n, s, angle ):
    other_angle = 180 - angle

    forward(n)
    left (angle)

    forward (s)
    left (other_angle)

    forward(n)
    left (angle)

    forward(s)
    left(other_angle)

def rectangle(wide, tall):
    paralelogram(wide, tall, 90)

def rombus (n, angle): 
    paralelogram (n, n, angle )

rombus(60, 50)
turtle.done()
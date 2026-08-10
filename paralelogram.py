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

paralelogram (60, 30, 50)
turtle.done()
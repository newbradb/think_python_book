import turtle

from turtle import forward, left

def rhombus (n, angle):
    other_angle = 180 - angle

    forward(n)
    left (angle)

    forward (n)
    left (other_angle)

    forward(n)
    left (angle)

    forward(n)
    left(other_angle)


rhombus (50, 50)
turtle.done()
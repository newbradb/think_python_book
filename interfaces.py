import turtle

from turtle import forward
from turtle import left, right


def polygon(n, length):
    angle = 360 /n
    for i in range(n):
        forward(length)
        left(angle)
  
polygon (n=11, length=30)
turtle.done()

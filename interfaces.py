import turtle

from turtle import forward
from turtle import left, right


def square(length):
    for i in range(4):
        forward(length)
        left(90)
  

square(100)
square(150)
turtle.done()

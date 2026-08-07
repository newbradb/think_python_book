import turtle

from turtle import forward
from turtle import left, right


def square(length):
    for i in range(4):
        forward(length)
        left(90)
    turtle.done ()

square(100)
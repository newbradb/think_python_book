import math
import turtle
from turtle import forward, left

def polygon (n, length):
    angle = 360 / n
    for i in range (n):
        forward (length)
        left (angle)

def circle (radius):
    circumference = 2 * math.pi * radius
    n = 30 
    length = circumference / n
    polygon (n, length)

circle (radius=30)
turtle.done()

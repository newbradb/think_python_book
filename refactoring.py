import math
import turtle
from turtle import forward, left

def polyline(n, length, angle): 
    """Draws line segments with the given length and angle between them

    n: integer number of line segments
    length: length of the line segments
    angle: angle between segments (in degreess)
    """
    for i in range (n):
        forward(length)
        left(angle)

def polygon (n, length):
    angle = 360.0 / n
    polyline (n, length, angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30 
    length = arc_length / n
    step_angle = angle / n
    polyline (n, length, step_angle)

def circle (radius):
    arc(radius, 360)

polygon(n=20, length=9)
arc (radius=70, angle=70)
circle(radius=10)
from turtle import *
import random

speed(999)
bgcolor('black')

b = 120

while b - 1:
    line_color = (random.random(), random.random(), random.random())
    fill_color = (random.random(), random.random(), random.random())

    color(line_color, fill_color)
    left(b)
    forward(b * 2.5)
    b = b + 0.1 
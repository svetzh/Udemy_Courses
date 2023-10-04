from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

directions = [0, 90, 180, 270]
for _ in range(100):
    tim.speed(5)
    tim.pensize(10)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))



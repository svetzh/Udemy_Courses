from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["cyan", "purple", "blue", "red", "green", "black", "DeepSkyBlue", "IndianRed", "DarkOrchid", "wheat"]
directions = [0, 90, 180, 270]
for _ in range(100):
    tim.speed(0)
    tim.pensize(7)
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


# tim.speed("fastest")
#
# def move_randomly(thickness):
#     tim.color(random.choice(colours))
#     tim.pensize(thickness)
#     distance = random.randint(10, 50)
#     tim.forward(distance)
#     tim.right(90)
#
# n = int(input("Set number of repetitions: "))
# for _ in range(n):
#     move_randomly(10)
#

screen = Screen()
screen.exitonclick()

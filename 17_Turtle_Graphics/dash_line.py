from turtle import Turtle, Screen

tim_turtle = Turtle()

tim_turtle.shape("turtle")
tim_turtle.color("green")
tim_turtle.pencolor("coral")
screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

for _ in range(50):
    tim_turtle.forward(10)
    tim_turtle.pu()
    tim_turtle.forward(10)
    tim_turtle.pd()

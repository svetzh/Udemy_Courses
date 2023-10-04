from turtle import Turtle, Screen

tim_turtle = Turtle()

tim_turtle.shape("turtle")
tim_turtle.color("green")
tim_turtle.pencolor("coral")
screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

screen = Screen()
screen.exitonclick()
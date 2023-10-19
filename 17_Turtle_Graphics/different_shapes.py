from turtle import Turtle, Screen

tr = Turtle()

def draw_shape(sides, color, thickness):
    tr.pencolor(color)
    tr.pensize(thickness)
    for _ in range(sides):
        tr.forward(100)
        tr.right(360/sides)

draw_shape(3, "green", 2)
draw_shape(4, "red", 2)
draw_shape(5, "blue", 2)
draw_shape(6, "yellow", 2)
draw_shape(8, "black", 2)
draw_shape(9, "orange", 2)
draw_shape(10, "purple", 2)

screen = Screen()
screen.exitonclick()

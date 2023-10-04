import random
import turtle as turtle_module

tim = turtle_module.Turtle()
tim.speed(0)
tim.pu()
tim.hideturtle()
turtle_module.colormode(255)

colors_list = [
    (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148),
    (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
    (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (32, 60, 109),
    (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49),
    (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113),
    (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)
]
tim.setheading(225)
tim.forward(300)

tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)


print(tim)

screen = turtle_module.Screen()
screen.exitonclick()
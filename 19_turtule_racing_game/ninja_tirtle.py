import random
from turtle import Turtle, Screen

def display_race_result(res_text, txt_color):
    result_display = Turtle()
    result_display.penup()
    result_display.hideturtle()
    result_display.goto(0, 0)
    result_display.color(txt_color)
    result_display.write(res_text, align="center", font=("Arial", 15, "normal"))

is_race_on = False
new_turtle = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter color: ")

colors = ["red", "green", "yellow", "orange", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
new_turtle.hideturtle()
turtles = []

for turtle_idx in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_idx])
    new_turtle.goto(x=-230, y=y_positions[turtle_idx])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > (screen.window_width() / 2):
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                result_text = f"You've won! {win_color} is winner!"
                text_color = win_color
            else:
                result_text = f"You've lost! {win_color} is winner!"
                text_color = win_color
            print(result_text)
            screen.clear()
            display_race_result(result_text, text_color)

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
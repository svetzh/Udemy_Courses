from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fd():
    tim.forward(10)

def move_bk():
    tim.backward(10)

def turn_right():
    new_head = tim.heading() - 10
    tim.setheading(new_head)

def turn_left():
    new_head = tim.heading() + 10
    tim.setheading(new_head)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()


screen.onkey(move_fd, "w")
screen.onkey(move_bk, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.listen()
screen.exitonclick()
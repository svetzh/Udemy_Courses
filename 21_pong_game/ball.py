from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def b_move(self):
        new_x = self.xcor() + self.x_move
        nex_y = self.ycor() + self.y_move
        self.goto(new_x, nex_y)

    def bounce_y(self):
        self.y_move *= -1  # reversing direction of y_move

    def bounce_x(self):
        self.x_move *= -1
        # only here we increase the speed when it hits a paddle
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        # here the speed should be reset to the initial one
        self.move_speed = 0.1
        self.bounce_x()





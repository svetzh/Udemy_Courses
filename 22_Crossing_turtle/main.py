import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_mgr = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(tim.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_mgr.create_car()
    car_mgr.move_cars()

    # Detect car collision
    for car in car_mgr.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False
            score.game_over()

    if tim.is_at_finish_line():
        tim.go_to_start()
        car_mgr.level_up()
        score.increase_level()




screen.exitonclick()
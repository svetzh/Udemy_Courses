import time
import turtle

from food import Food
from snake import Snake
from turtle import Screen
from score_board import Score

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 \
            or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor('black')
screen.title('My Snake Game')
game_is_on = True

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
scoreboard.score()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    scoreboard.score()
    snake.move()
    screen.update()
    time.sleep(0.1)
    if snake.snake_body[0].distance(food) < 15:
        scoreboard.increase_score()
        food.move()
        snake.new_body()
    if snake.collision():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()

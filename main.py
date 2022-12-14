import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# Score Tracker
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.total_score(score)
        snake.extend()

    # Detect Wall collision
    if snake.wall_collision():
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision with Snake itself
    for block in snake.snake_blocks[1:]:
        if snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

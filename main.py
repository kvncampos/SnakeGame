import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
counter = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # scoreboard.score(counter)

    # Detect collision with Food.
    if snake.head.distance(food) < 15:
        food.refresh()
        counter += 1
        scoreboard.undo()
        scoreboard.score(counter)



screen.exitonclick()

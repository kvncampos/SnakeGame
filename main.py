import time
import json
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, HighScore
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

username = simpledialog.askstring("Username", "Please enter your username: ")

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game v1")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
high_score_leader = HighScore()

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
            
# Read high scores from the file
with open("high_score.json", 'r') as f:
    high_score_data = json.load(f)

# Update the high score and username if the new score is higher
if score > high_score_data["current_high_score"]:
    high_score_data["current_high_score"] = score
    high_score_data["username"] = username

    # Write the updated data back to the file
    with open("high_score.json", 'w') as f:
        json.dump(high_score_data, f)

screen.exitonclick()

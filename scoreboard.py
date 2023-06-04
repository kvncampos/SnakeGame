from turtle import Turtle
import json

ALIGN = "center"
FONT = ('Arial', 14, 'normal')


class Scoreboard(Turtle):
    """Initiates Scoreboard starting from 0 at top of screen."""

    def __init__(self):
        super().__init__()
        # Draw the score on the screen
        self.hideturtle()
        self.penup()
        self.score = 0
        self.setposition(-200, 280)
        self.color("white")
        self.score_string = ""
        self.score_string = "Score: %s" % self.score
        self.write(self.score_string, False, align=ALIGN, font=FONT)

    def total_score(self, score):
        """Tracks Total Score when Snake Eats Food via counter"""
        self.score = score
        self.undo()
        self.score_string = "Score: %s" % self.score
        self.write(self.score_string, False, align=ALIGN, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over.", False, align="center", font=('Arial', 14, 'normal'))


class HighScore(Turtle):
    """HighScore Tracker, Reads from high_score.json file"""
    def __init__(self):
        super().__init__()
        self.high_score = 0  # Default value if not loaded from JSON
        self.username = ""  # Default value if not loaded from JSON
        self.hideturtle()
        self.penup()
        self.score = 0
        self.setposition(200, 280)
        self.color("white")
        self.load_high_score()

    def load_high_score(self):
        try:
            with open("high_score.json", 'r') as f:
                high_score_data = json.load(f)
                self.high_score = high_score_data["current_high_score"]
                self.username = high_score_data["username"]
        except FileNotFoundError:
            print("JSON file not found.")
        except KeyError:
            print("Invalid JSON file format.")

        self.write(f"Current HighScore: {self.high_score} by {self.username}", False, align="right", font=FONT)

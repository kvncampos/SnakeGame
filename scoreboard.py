from turtle import Turtle, Screen

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
        self.setposition(0, 280)
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

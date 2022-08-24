from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Draw the score on the screen
        self.points = None
        self.score_string = ""

    def score(self, points):
        self.points = points
        self.hideturtle()
        self.penup()
        self.setposition(0, 280)
        self.color("white")
        self.score_string = "Score: %s" % self.points
        self.write(self.score_string, False, align='center', font=('Arial', 14, 'normal'))

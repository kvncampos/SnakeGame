from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

        # Creates Snake Blocks

    def create_snake(self):
        """Creates new snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates new snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_blocks.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_blocks[-1].position())

    def move(self):
        """Defines the movement of the snake by moving last block"""
        for block_num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[block_num - 1].xcor()
            new_y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def wall_collision(self):
        """checks for wall collisions """
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            wall = Turtle()
            wall.hideturtle()
            wall.color("White")
            return True



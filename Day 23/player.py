# Player Class - Controls the player's turtle character
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)  # Point turtle upward
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)  # Start at bottom center

    def move_up(self):
        # Move turtle upward by fixed distance
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def starting_position(self):
        # Reset turtle to starting position for new level
        self.goto(STARTING_POSITION)

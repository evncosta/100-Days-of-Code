# Paddle Class - Creates and controls paddle movement for Pong game
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Make paddle tall and thin
        self.penup()
        self.goto(position)  # Set initial position

    def go_up(self):
        # Move paddle up by 25 pixels
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Move paddle down by 25 pixels
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)

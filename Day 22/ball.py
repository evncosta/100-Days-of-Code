# Ball Class - Handles ball movement, bouncing, and reset for Pong game
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10  # Horizontal movement speed
        self.y_move = 10  # Vertical movement speed
        self.move_speed = 0.1  # Controls game speed through sleep time

    def move(self):
        # Update ball position based on current movement values
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Reverse vertical direction (top/bottom wall collision)
        self.y_move *= -1

    def bounce_x(self):
        # Reverse horizontal direction and increase speed (paddle collision)
        self.x_move *= -1
        self.move_speed *= 0.9  # Gradually increase game speed

    def reset_position(self):
        # Return ball to center and reset speed after scoring
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()  # Send ball toward opposite player

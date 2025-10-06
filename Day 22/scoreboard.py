# Scoreboard Class - Displays and updates scores for Pong game
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()  # Hide turtle cursor
        self.l_score = 0   # Left player score
        self.r_score = 0   # Right player score
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear and redraw scores on screen
        self.clear()
        # Display left player score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "bold"))
        # Display right player score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "bold"))

    def l_point(self):
        # Increment left player score and update display
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # Increment right player score and update display
        self.r_score += 1
        self.update_scoreboard()
      

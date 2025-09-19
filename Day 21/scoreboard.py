# Scoreboard Class - Displays and manages game score
from turtle import Turtle

# Constants for text formatting
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize score counter
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Position scoreboard at top of screen
        self.update_scoreboard()
        self.hideturtle()  # Hide turtle cursor

    def update_scoreboard(self):
        # Display current score
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # Display game over message at center of screen
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Increment score and update display
        self.score += 1
        self.clear()  # Clear previous score
        self.update_scoreboard()

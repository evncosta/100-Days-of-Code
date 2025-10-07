# Scoreboard Class - Displays game level and game over message
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-290, 260)  # Position in top-left corner
        self.color("black")
        self.penup()
        self.hideturtle()  # Hide turtle cursor
        self.player_score = 0  # Track current level
        self.update_scoreboard()

    def update_scoreboard(self):
        # Clear and redraw current level
        self.clear()
        self.write(f"Level:{self.player_score}", font=FONT)

    def player_point(self):
        # Increase level counter and update display
        self.player_score += 1
        self.update_scoreboard()

    def game_over(self):
        # Display game over message at center of screen
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

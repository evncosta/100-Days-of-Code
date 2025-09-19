# Food Class - Handles food appearance and positioning for Snake game
from turtle import Turtle
import random

# Color palette for food items
food_colors = ["#FF4F58", "#FF8C00", "#FFFA4D", "#A7E35F", "#00BFFF", "#4169E1", "#DF00FF", "#FF69B4", "#00FFFF",
               "#FFD700"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller than snake segments
        self.speed("fastest")
        self.refresh()  # Set initial position and color

    def random_color(self):
        # Select random color from palette
        return random.choice(food_colors)

    def refresh(self):
        # Move food to random position within game boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        # Apply new random color
        self.color(self.random_color())

from turtle import Turtle
import random

food_colors = ["#FF4F58", "#FF8C00", "#FFFA4D", "#A7E35F", "#00BFFF", "#4169E1", "#DF00FF", "#FF69B4", "#00FFFF",
               "#FFD700"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def random_color(self):
        return random.choice(food_colors)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.color(self.random_color())
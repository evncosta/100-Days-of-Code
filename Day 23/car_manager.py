# CarManager Class - Handles car generation, movement, and difficulty scaling
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []  # List to store all active cars
        self.starting_speed = STARTING_MOVE_DISTANCE  # Initial car speed
        self.increment = MOVE_INCREMENT  # Speed increase amount per level

    def add_car(self):
        # Random chance to generate a new car (1 in 6 probability)
        car_chance = random.randint(1, 6)
        if car_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))  # Random car color
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # Make car rectangular
            random_y = random.randint(-250, 250)  # Random lane position
            new_car.goto(300, random_y)  # Start at right edge of screen
            self.cars.append(new_car)

    def increase_speed(self):
        # Increase car speed when player advances level
        self.starting_speed += self.increment

    def move_car(self):
        # Move all cars from right to left across screen
        for car in self.cars:
            car.backward(self.starting_speed)

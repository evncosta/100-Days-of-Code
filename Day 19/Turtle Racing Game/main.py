# Turtle Racing Game - Bet on which colored turtle will win the race
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Get user's bet on winning turtle color
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Choose a color (red/orange/yellow/green/blue/purple): ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Create and position racing turtles
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=turtle_index * 30 - 80)  # Line up turtles at start
    t.pendown()
    turtles.append(t)

# Start race if user made a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:
    for turtle in turtles:
        # Check if turtle has reached finish line
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            # Compare winner with user's bet
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
                is_race_on = False
        # Move each turtle forward by random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Keep window open until clicked
screen.exitonclick()

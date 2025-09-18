# Snake Game - Main game loop and screen setup
from turtle import Screen
from snake import Snake
import time

# Set up game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize snake object
snake = Snake()

# Set up keyboard controls for snake movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

# Main game loop
while game_is_on:
    screen.update()  # Manual screen refresh
    time.sleep(0.1)  # Control game speed
    snake.move()     # Update snake position

# Keep window open until clicked
screen.exitonclick()

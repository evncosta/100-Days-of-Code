# Snake Game - Complete game with food, scoring, and collision detection
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()      # Move food to new location
        snake.extend()      # Add new segment to snake
        scoreboard.increase_score()  # Update score
        scoreboard.update_scoreboard()  # Refresh score display

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with own tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Keep window open until clicked
screen.exitonclick()

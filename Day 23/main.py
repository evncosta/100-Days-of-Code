# Turtle Crossing Game - Main game loop for road crossing challenge
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Set up player controls
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(0.1)  # Control game speed
    screen.update()  # Refresh screen

    # Manage car generation and movement
    car_manager.add_car()
    car_manager.move_car()

    # Check if player reached finish line
    if player.ycor() > 310:
        scoreboard.player_point()      # Increase score
        player.starting_position()     # Reset player position
        car_manager.increase_speed()   # Increase difficulty

    # Check for collision with any car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

# Keep window open until clicked
screen.exitonclick()

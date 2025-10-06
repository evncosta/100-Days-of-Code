# Pong Game - Main game loop and setup for two-player paddle game
import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set up game screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
turtle.tracer(0)  # Turn off automatic screen updates

# Initialize game objects
r_paddle = Paddle((350, 0))  # Right paddle
l_paddle = Paddle((-350, 0)) # Left paddle
ball = Ball()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")    # Right paddle up
screen.onkey(r_paddle.go_down, "Down") # Right paddle down
screen.onkey(l_paddle.go_up, "w")     # Left paddle up
screen.onkey(l_paddle.go_down, "s")   # Left paddle down

game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(ball.move_speed)  # Control game speed
    screen.update()              # Refresh screen
    ball.move()                  # Update ball position

    # Detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss (left player scores)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss (right player scores)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# Keep window open until clicked
screen.exitonclick()

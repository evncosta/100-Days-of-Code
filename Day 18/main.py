# The Hirst Painting Project - Creates a grid of colored dots using Turtle graphics
import turtle
import random

# Color palette for the dots (RGB tuples)
colors = [(242, 117, 31), (240, 79, 94), (255, 140, 0), (154, 113, 8), (128, 215, 206), 
          (212, 153, 163), (150, 186, 224), (167, 45, 137), (51, 91, 86), (85, 183, 4), 
          (255, 105, 180), (132, 218, 221), (249, 207, 0), (200, 100, 120), (211, 130, 19), 
          (246, 208, 47), (134, 188, 147), (229, 168, 179), (173, 216, 230), (164, 190, 224), 
          (65, 105, 100), (255, 215, 0), (138, 43, 226), (116, 94, 6), (255, 165, 0), 
          (75, 0, 130), (180, 60, 110), (95, 160, 190), (220, 90, 60), (145, 200, 80)]

# Set up turtle and screen
t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)  # Enable RGB color mode

screen = turtle.Screen()
screen.setup(width=500, height=500)

# Grid configuration
dot_size = 25
spacing = dot_size * 2

# Calculate starting position for grid
width = screen.window_width()
height = screen.window_height()
x_start = -width / 2 + dot_size
y_start = -height / 2 + dot_size

# Hide turtle and position at start
t.hideturtle()
t.penup()
t.goto(x_start, y_start)

# Create 10x10 grid of colored dots
for _ in range(10):
    for i in range(10):
        t.dot(dot_size, random.choice(colors))  # Draw random colored dot
        if i < 9:
            t.forward(spacing)  # Move to next column
    # Return to start of row and move down
    t.backward(spacing * 9)
    t.left(90)
    t.forward(spacing)
    t.right(90)

# Keep window open until click
screen.exitonclick()


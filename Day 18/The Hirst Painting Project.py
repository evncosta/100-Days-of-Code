import turtle
import random

colors = [(242, 117, 31), (240, 79, 94), (255, 140, 0), (154, 113, 8), (128, 215, 206), (212, 153, 163), (150, 186, 224), (167, 45, 137), (51, 91, 86), (85, 183, 4), (255, 105, 180), (132, 218, 221), (249, 207, 0), (200, 100, 120), (211, 130, 19), (246, 208, 47), (134, 188, 147), (229, 168, 179), (173, 216, 230), (164, 190, 224), (65, 105, 100), (255, 215, 0), (138, 43, 226), (116, 94, 6), (255, 165, 0), (75, 0, 130), (180, 60, 110), (95, 160, 190), (220, 90, 60), (145, 200, 80)]

t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)

screen = turtle.Screen()
screen.setup(width=500, height=500)

dot_size = 25
spacing = dot_size * 2

width = screen.window_width()
height = screen.window_height()
x_start = -width / 2 + dot_size
y_start = -height / 2 + dot_size

t.hideturtle()
t.penup()
t.goto(x_start, y_start)

for _ in range(10):
    for i in range(10):
        t.dot(dot_size,random.choice(colors))
        if i < 9:
            t.forward(spacing)
    t.backward(spacing * 10 - spacing)
    t.left(90)
    t.forward(spacing)
    t.right(90)

screen.exitonclick()
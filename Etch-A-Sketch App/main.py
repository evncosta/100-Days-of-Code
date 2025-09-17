```python
# Turtle Drawing Program - Interactive drawing with keyboard controls
from turtle import Turtle, Screen

# Initialize turtle and screen
t = Turtle()
screen = Screen()

# Movement functions for turtle control
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def clear_screen():
    t.clear()    # Clear all drawings
    t.penup()    # Lift pen to move without drawing
    t.home()     # Return to center (0,0)
    t.pendown()  # Lower pen to resume drawing

# Set up keyboard event listeners
screen.listen()
screen.onkey(key="w", fun=move_forward)  # Move forward with W key
screen.onkey(key="s", fun=move_backward) # Move backward with S key
screen.onkey(key="a", fun=move_left)     # Turn left with A key
screen.onkey(key="d", fun=move_right)    # Turn right with D key
screen.onkey(key="c", fun=clear_screen)  # Clear screen with C key

# Keep window open until clicked
screen.exitonclick()
```

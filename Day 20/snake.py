# Snake Class - Handles snake creation, movement, and controls
from turtle import Turtle

# Constants for snake configuration
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]  # Reference to the head segment

    def create_snake(self):
        # Create initial snake with 3 segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Create and configure a new snake segment
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        # Add new segment to the end of the snake
        self.add_segment(self.body[-1].position())

    def move(self):
        # Move snake body segments from tail to head
        for segment_number in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment_number - 1].xcor()
            new_y = self.body[segment_number - 1].ycor()
            self.body[segment_number].goto(new_x, new_y)
        # Move head forward
        self.body[0].forward(MOVE_DISTANCE)

    # Direction control methods with prevention of 180° turns
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

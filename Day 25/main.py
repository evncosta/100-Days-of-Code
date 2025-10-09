# U.S. States Game - Interactive geography quiz with turtle graphics
import turtle
import pandas

# Set up game screen with map background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load state data and prepare game variables
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop - continue until all states are guessed
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    
    # Handle exit command and generate learning list
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        # Save unguessed states to CSV file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    # Check if answer is correct and display state name on map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # Get coordinates for state and display name
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

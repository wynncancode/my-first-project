#TODO-1: Set up the screen with background image
#TODO-2: Convert the guess to Title case
#TODO-3: Check if the guess is among the 50 states
#TODO-4: Write correct guesses onto the map
#TODO-5: Use a loop to allow the user to keep guessing
#TODO-6: Record the correct guesses in a list
#TODO-7: Keep track of the score

import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

#Add the image to the screen and change the shape of the turle to image.
screen.addshape(image)
turtle.shape(image)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state_t = answer_state.title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    if answer_state_t == "Exit":
        break
    if answer_state_t in all_states:
        guessed_states.append(answer_state_t)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state_t]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

#create all the unguess states into a csv file
states_to_learn = []
for state in all_states:
    if state not in guessed_states:
        states_to_learn.append(state)
new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")

#turtle.mainloop()
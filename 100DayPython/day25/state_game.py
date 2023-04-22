import turtle
import pandas as pd

image = "blank_states_img.gif"
path = "50_states.csv"
correct_state = []
data = pd.read_csv(path)

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)

while(len(correct_state) <= 20):
    answer_state = screen.textinput(title=f"Guess the State {len(correct_state)}/50", prompt="What's another state's name?").lower()
    state_find = data[data['state'].str.lower() == answer_state]
    if(len(state_find) > 0 and answer_state not in correct_state):
        correct_state.append(answer_state)
        posX = state_find.iloc[0, 1]
        posY = state_find.iloc[0, 2]
        print(posX, posY)

        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(posX, posY)
        text.write(answer_state, True, align="center", font=('Arial', 12, 'bold'))


turtle.mainloop()

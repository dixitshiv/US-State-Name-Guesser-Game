import turtle
import pandas
screen = turtle.Screen()
screen.title('US State Game')
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data["state"].tolist()

guessed_state = []

while len(guessed_state) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_state)}/50 guessed correctly. US State Game", prompt="Enter name of the state: ").title()
    if (ans_state == "Exit"):
        break
    if ans_state in state_names:
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(ans_state)



not_guessed_state = []
for state in state_names:
    if state not in guessed_state:
        not_guessed_state.append(state)

tolearn = pandas.DataFrame(not_guessed_state)
tolearn.to_csv("States_to_learn.csv")
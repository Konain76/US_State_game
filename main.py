import turtle
import pandas

screen = turtle.Screen()
screen.title("US-state-game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
# find_ans_state = data[data["state"] == answer_state]
# print(find_ans_state)
# ans_state_xcor = int(find_ans_state["x"])
# ans_state_ycor = int(find_ans_state["y"])
# pos_of_ans_state = turtle.Turtle()
# pos_of_ans_state.shape("arrow")
# pos_of_ans_state.goto(x=ans_state_xcor, y=ans_state_ycor)
all_states = data.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct",
                                    prompt="whats's another state?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        find_ans_state = data[data["state"] == answer_state]

        x_cor = int(find_ans_state["x"])
        y_cor = int(find_ans_state["y"])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(answer_state)
states_to_learn = [all_states[i] for i in range(len(all_states)) if all_states[i] not in guessed_state]
# for i in range(len(all_states)):
#
#     if all_states[i] in guessed_state:
#         passoo
#     else:
#         states_to_learn.append(all_states[i])
state_dict = {
    "Missing_state": states_to_learn
}
Missing_state_data = pandas.DataFrame(state_dict)
Missing_state_data.to_csv("states_to_learn.csv")
print(Missing_state_data)

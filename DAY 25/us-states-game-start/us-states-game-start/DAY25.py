import turtle 
import pandas as pd
data = pd.read_csv("us-states-game-start\\us-states-game-start\\50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "us-states-game-start\\us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

space = []
game = True
score = 0 
home = data.state.to_list()
num = len(home)

while len(space) < 50 :
    answer_state = screen.textinput(  f"{score}/{num} States", "What's another state's name?").title()
    if answer_state == "Exit":
        answer = []
        for state in home:
            if state not in space:
                answer.append(state)
        bus = pd.DataFrame(answer)
        bus.to_csv("us-states-game-start\\us-states-game-start\\states_to_learn.csv")
        break
    if answer_state in home:
        score += 1 
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        UP = data[data.state == answer_state]
        t.goto(int(UP.x),int(UP.y))
        t.write(answer_state)
        space.append(answer_state)



# states_to_learn.csv

    

# screen.exitonclick()
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)






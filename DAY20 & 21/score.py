from turtle import Turtle 
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt")  as file:
            self.high = int(file.read())
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_scoreboard()
    
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}" f" High Score: {self.high}", align = ALIGNMENT, font = FONT)
    
    def reset(self):
        if self.score > self.high:
            self.high = self.score
            with open('data.txt', mode = 'w') as file:
                file.write(f" {self.high} ")


        self.score = 0 
        self.update_scoreboard
    
    
    def new_score(self):
        self.score += 1 
        self.update_scoreboard()
        
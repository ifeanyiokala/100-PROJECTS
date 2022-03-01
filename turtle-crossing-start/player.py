from turtle import Turtle 
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.tron = 0.1
        self.score = 0 

    def up(self):
        self.forward(MOVE_DISTANCE)

      
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER, FINAL SCORE : {self.score}",align="center", font=44)
        
    def restart(self):
        self.goto(STARTING_POSITION)
        self.tron -= 0.01

    def score(self):
        self.score += 1 
        self.restart()

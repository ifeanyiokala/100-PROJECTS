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
        self.restart()
        

    def up(self):
        self.forward(MOVE_DISTANCE)


    def restart(self):
        self.goto(STARTING_POSITION)

    def score(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
      
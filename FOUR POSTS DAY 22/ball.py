from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 20
        self.tron = 0.1
       
        # self.home()
       

    def move(self):
        new_x = self.xcor() + self.x_move #random.randint(-350,350)
        new_y = self.ycor() + self.y_move #random.randint(-250,250)
        self.goto(new_x,new_y)
        # random_x = random.randint(-350,350)
        # random_y = random.randint(-250,250)
        # self.goto(random_x,random_y)

    def bounce_1(self):
        self.y_move *= -1
        self.tron -= 0.004
    
    def bounce_2(self):
        self.x_move *= -1
        self.tron -= 0.004

    def restart(self):
        self.goto(0,0)
        self.bounce_2()
        self.tron = 0.1

    def restart_2(self):
        self.goto(0,0)
        self.bounce_1()
        self.tron = 0.1

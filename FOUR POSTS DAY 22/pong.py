from turtle import Turtle 

class Pong(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid =5,stretch_len =1 )
        self.penup()
        self.goto(x,y)
    
    
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)  

class Pong_h(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid =5,stretch_len =1 )
        self.penup()
        self.goto(x,y)

    def go_right(self):
        new_r = self.xcor() + 30
        self.goto(new_r,self.ycor())

    def go_left(self):
        new_l = self.xcor() - 30
        self.goto(new_l,self.ycor())  


    




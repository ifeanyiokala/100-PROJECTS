from turtle import Screen,Turtle
from pong import Pong,Pong_h
from ball import Ball
from scoreboard import Scoreboard
import time


screen  = Screen ()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Four Posts")
screen.tracer(0)


pg = Pong(350,0)
pg_2 = Pong(-350,0)
pg_3 = Pong_h(0,260)
pg_4 = Pong_h(0,-260)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(pg.go_up,"Up")
screen.onkey(pg.go_down,"Down")
screen.onkey(pg_2.go_up,"e")
screen.onkey(pg_2.go_down,"d")
screen.onkey(pg_3.go_right,"f")
screen.onkey(pg_3.go_left,"s")
screen.onkey(pg_4.go_right,"Right")
screen.onkey(pg_4.go_left,"Left")

game_is_on = True 
while game_is_on:
    time.sleep(ball.tron)
    screen.update()
    ball.move()

    
    #Detect collision with paddles on the horizontal axis 
    if ball.distance(pg) < 50 and ball.xcor() > 320 or ball.distance(pg_2) < 50 and ball.xcor() < - 320 :
        ball.bounce_2()
        ball.speed()
    #Detetct collison with paddles on the vertical axis 
    if ball.distance(pg_3) < 50 and ball.ycor() > 250 or ball.distance(pg_4) < 50 and ball.ycor() < - 250 :
        ball.bounce_1() 
        ball.speed()
    
    #Detect if the ball goes out of bounds and also give out points 
    if ball.xcor() > 380  :
        ball.restart()
        scoreboard.l_point()

    if ball.ycor() < -280 :
        ball.restart_2()
        scoreboard.l_point()


    if ball.xcor() < -380 :
        ball.restart()
        scoreboard.r_point() 
    
    
    if ball.ycor() > 280:
        ball.restart_2()
        scoreboard.r_point()






screen.exitonclick()





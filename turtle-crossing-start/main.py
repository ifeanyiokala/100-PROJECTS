import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()


screen.listen()
screen.onkey(player.up,"Up")
cm = CarManager()




game_is_on = True
while game_is_on:
    time.sleep(player.tron)
    screen.update()
    cm.new_car()
    cm.move_cars()

    for car in cm.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            player.game_over()

            
        if player.ycor() > 260:
            player.restart()
            player.score()

#     time.sleep(0.9)
# #     cm.dar()
# #     cm.many_cars()
#     cm.moved()

#     if cm.xcor() < -290:
#         cm.bk(600)


screen.exitonclick()
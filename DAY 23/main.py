import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Avoid The Missle")
cm = CarManager()
player = Player()
sb = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cm.new_car()
    cm.move_cars()

    for car in cm.all_cars:
        if car.distance(player) < 15:
            game_is_on = False
            sb.game_over()

    if player.score():
        player.restart()
        cm.jump_up()
        sb.increase_level()

#     time.sleep(0.9)
# #     cm.dar()
# #     cm.many_cars()
#     cm.moved()

#     if cm.xcor() < -290:
#         cm.bk(600)


screen.exitonclick()
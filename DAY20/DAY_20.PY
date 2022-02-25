# from tracemalloc import stop
from turtle import Screen ,Turtle, update
import time 
from snake import Snake


tm = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

tm.shape('square')
tm.color('white')
tm.shapesize(stretch_wid=2,stretch_len=2)
tm.hideturtle()

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# for turtle_index in X_positions:
#     tm = Turtle(shape="square")
#     tm.color('white')
#     tm.penup()
#     tm.goto(turtle_index)
#     segments.append(tm)


game_is_on = True 
while game_is_on:
     screen.update()
     time.sleep(0.1)

     snake.move()





#     for seg_num in range(len(segments)-1,0,-1):
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y) 
#     segments[0].forward(20)


screen.exitonclick()

    
# for seg_num in range(len(segments) - 3, 2,1):
#     new_x = segments[seg_num + 1].xcor()
#     new_y = segments[seg_num + 1].ycor()
#     segments[seg_num].goto(new_x, new_y) 
# segments[0].forward(20)
    # segments[0].left(90)
        
























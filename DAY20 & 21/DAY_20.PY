#imported the needed modules
from turtle import Screen ,Turtle, update
import time 
from snake import Snake
from food import Food
from score import Score

#set the screen enviroment and color 
tm = Turtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#set the snanke color and size,plus i hid the turtle :)
tm.shape('square')
tm.color('white')
tm.shapesize(stretch_wid=2,stretch_len=2)
tm.hideturtle()

#called the needed classes
score = Score()
snake = Snake()
food = Food()


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

     #Detect collision with food.
     if snake.head.distance(food) < 15:
          food.refresh()
          snake.extend()
          score.new_score()

     #Allows the snake to pas through the walls and return at the reverse direction.
     if snake.head.xcor() > 299  or snake.head.xcor() < -290  or  snake.head.ycor() > 299 or  snake.head.ycor() < -299 :
          snake.head.bk(599)     
          # new = snake.head.pos()
          # snake.head.goto(-new.xcor(),new.ycor())

     #Detect collision with tail.
     for segment in snake.segments[1:]:
          if snake.head.distance(segment) < 10:
               game_is_on = False 
               score.game_over()


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
        
























import turtle as turtle_module  

import heroes
import random
import colorgram 

# rgb_colors = []
# colors = colorgram.extract("heist.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
tm = turtle_module.Turtle()
turtle_module.colormode(255)
tm.right(90)
tm.penup()
tm.forward(200)
tm.left(90)

tm.hideturtle()
life = True 
scope = 0  
color_list = [(245, 248, 253), (244, 235, 46), (196, 12, 34), (221, 159, 69), (43, 80, 178), (238, 39, 143), (40, 215, 68), (238, 229, 5), (30, 40, 154), (23, 147, 26), (207, 74, 22), (202, 34, 91), (186, 16, 9), (19, 18, 42), (216, 141, 191), (57, 15, 10), (88, 8, 28), (227, 161, 9), (78, 212, 157), (67, 73, 221), (13, 95, 61), (78, 194, 225), (239, 158, 
215), (94, 233, 204), (220, 76, 48), (15, 67, 46), (7, 226, 238)]



while life :
    scope += 1 
    for key in color_list[0:10]:
            tm.dot(20,random.choice(color_list))
            tm.penup()
            tm.forward(50)

    tm.setheading(90)
    tm.forward(50)
    tm.setheading(180)
    tm.forward(500)
    tm.setheading(0)

if scope == 10:
    life = False 

screen = turtle_module.Screen()
screen.setup(900,900)
screen.exitonclick()

# print(rgb_colors)

# tm.width(4)
# tm.pensize(4)
# tm.shape("turtle")
# tm.color("green")
# tm.speed(10)
# print(heroes.gen())


no_sides = 2 

def draw_shape(no_sides):
    for _ in range(no_sides) : 
        deg = 360 / no_sides
        tm.forward(100)
        tm.right(deg)


# motion = [0,90,180,270]
# for _ in range (100) :
#     tm.forward(random.choice(motion))
#     tm.right(random.choice(motion))
#     tm.left(random.choice(motion))
#     tm.backward(random.choice(motion))


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tm.color(R, G, B)




# for _ in range(200) : 
#     tm.circle(100)
#     tm.left(10)
#     tm.hideturtle()
#     change_color()
# for shape_of_side in range(3,11):
#     draw_shape(shape_of_side)
#     change_color()












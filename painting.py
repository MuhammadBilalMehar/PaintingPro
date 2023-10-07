# import colorgram


# rgb_colors =[]
# colors = colorgram.extract('img.jpg',20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as t
from turtle import Screen
import random

color_list = [(34, 103, 181), (52, 196, 32), (168, 166, 28), (158, 18, 116), (234, 137, 42), (159, 94, 29), (41, 184, 232), (150, 48, 129), (26, 35, 68), (47, 42, 135), (13, 188, 228), (60, 39, 19), (59, 23, 52), (42, 119, 226), (43, 128, 49), (204, 236, 8), (21, 53, 26), (246, 88, 20), (210, 238, 26), (182, 46, 184)]

tur = t.Turtle()
t.colormode(255)
sc = Screen()
tur.penup()
tur.hideturtle()
tur.speed("fastest")
tur.setheading(225)
tur.forward(300)
tur.setheading(0)
no_of_dots = 100

for dot_count in range(1,no_of_dots+1): 
    tur.dot(20,random.choice(color_list))
    tur.forward(50)

    if dot_count % 10 == 0:
        tur.setheading(90)
        tur.forward(50)
        tur.setheading(180)
        tur.forward(500)
        tur.setheading(0)




sc.exitonclick()

import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

'''
rgb_colors = []
colors = colorgram.extract('StarryNight.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
'''

color_list = [(42, 106, 144), (16, 42, 61), (109, 165, 189), (23, 47, 42), (138, 176, 158), (76, 102, 90), (72, 147, 172), (51, 45, 37), (14, 65, 123), (177, 177, 121), (98, 95, 67), (206, 210, 136), (197, 223, 204), (222, 227, 188), (21, 79, 97), (182, 217, 232), (167, 207, 180), (182, 162, 42), (43, 75, 65), (98, 146, 134), (156, 204, 218), (34, 28, 32), (84, 131, 177), (72, 74, 40), (91, 83, 87), (85, 55, 47), (164, 193, 224), (155, 149, 153), (232, 226, 230), (73, 58, 62)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()

for i in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.backward(50)
    tim.pendown()
    if i%2 == 0:
        tim.left(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.left(90)
    else:
        tim.right(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.right(90)

screen = turtle_module.Screen()
screen.exitonclick()
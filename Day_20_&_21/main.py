from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("Black")
screen.tracer(0)
screen.title("My Snake Game")

starting_position = [(0,0), (-20,0), (-40,0)]

segments =[]

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()
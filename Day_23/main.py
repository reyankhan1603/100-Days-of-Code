import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()

game_is_on = True
while game_is_on:

    screen.onkey(player.move, "Up")
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 270:
        player.finishline()
        game_is_on = False


screen.exitonclick()
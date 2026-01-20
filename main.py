import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_mngr = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_mngr.make_new_car()

    car_mngr.move_cars()

    for car in car_mngr.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        scoreboard.level_up()
        car_mngr.level_up()



screen.exitonclick()
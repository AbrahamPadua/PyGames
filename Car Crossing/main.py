from turtle import Screen, Turtle
from player import Player
from level import Level
from cars import Car_Manager
import time

screen = Screen()
screen.title("Crossing Turtle")
screen.setup(width=900, height=600)
screen.tracer(0)


def increase_level():
    level.level += 1
    level.update_level()
    cars.increase_level()
    turtle.goto(0, -260)


def start():
    global turtle
    turtle = Player()
    global cars
    cars = Car_Manager()
    global level
    level = Level()

    screen.listen()
    screen.onkey(turtle.move_up, "w")
    screen.onkey(turtle.move_left, "a")
    screen.onkey(turtle.move_right, "d")

    speed = 0.1
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(speed)
        if len(cars.cars) < 20:
            cars.generate_cars()
        cars.move_cars()

        if turtle.ycor() >= 290:
            level.level_cleared()
            time.sleep(0.7)
            speed -= speed * 0.1
            increase_level()

        for car in cars.cars:
            if turtle.distance(car) <= 20:
                level.game_over()
                screen.onkeyrelease(restart, "r")
                game_is_on = False

        def restart():
            level.clear()
            turtle.hideturtle()
            for car in cars.cars:
                car.hideturtle()
            start()


start()

screen.exitonclick()

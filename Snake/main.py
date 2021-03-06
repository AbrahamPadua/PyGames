from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)


def start():
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.segments[0].distance(food) < 15:
            food.new_position()
            scoreboard.score += 1
            scoreboard.update_score()
            snake.extend()

        if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < - 290:
            game_is_on = False

        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False

    def restart():
        for segments in snake.segments:
            segments.hideturtle()
        scoreboard.clear()
        food.hideturtle()
        start()

    scoreboard.game_over()
    screen.onkeypress(restart, "r")


start()
screen.exitonclick()

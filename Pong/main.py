from turtle import Screen, Turtle
from players import Player1, Player2
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

p1 = Player1()
p2 = Player2()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(p1.move_up, "w")
screen.onkeypress(p1.move_down, "s")
screen.onkeypress(p2.move_up, "Up")
screen.onkeypress(p2.move_down, "Down")

y_cor = -260
while y_cor < 280:
    line = Turtle("square")
    line.color("white")
    line.penup()
    line.shapesize(stretch_len=0.1, stretch_wid=0.5)
    line.goto(0, y_cor)
    y_cor += 20

game_is_on = True
while game_is_on:
    time.sleep(ball.ms)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.ybounce()

    if (ball.distance(p2) < 53 and ball.xcor() > 350) or (ball.distance(p1) < 53 and ball.xcor() < -360):
        ball.xbounce()

    if ball.xcor() >= 390:
        scoreboard.p2_score += 1
        scoreboard.update_point()
        ball.reset_pos()

    if ball.xcor() <= -395:
        scoreboard.p1_score += 1
        scoreboard.update_point()
        ball.reset_pos()

screen.exitonclick()

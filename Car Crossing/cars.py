from turtle import Turtle
import random

CARS = {"red": 20, "yellow": 15, "green": 10, "blue": 5}


class Car_Manager:
    def __init__(self):
        self.red_chance = 5
        self.yellow_chance = 10
        self.green_chance = 25
        self.blue_chance = 60
        self.cars = []

    def increase_level(self):
        rand = random.uniform(0, 0.1)
        increase_red = self.green_chance * rand
        self.red_chance += increase_red
        self.green_chance -= increase_red
        increase_yellow = self.blue_chance * rand
        self.yellow_chance += increase_yellow
        self.blue_chance -= increase_yellow
        for car in CARS:
            CARS[car] += 1

    def generate(self, color):
        car = Turtle("square")
        car.color(color)
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.goto(450, random.randrange(-210, 210, 50))
        self.cars.append(car)

    def generate_cars(self):
        generate_chance = random.randint(1, 6)
        if generate_chance == 1:
            color = random.randint(1, 99)
            if color <= self.red_chance:
                self.generate("red")
            elif color <= self.yellow_chance:
                self.generate("yellow")
            elif color <= self.green_chance:
                self.generate("green")
            else:
                self.generate("blue")

    def move_cars(self):
        for car in self.cars:
            color = car.color()[0]
            car.back(CARS[color])
            if car.xcor() < -470:
                self.cars.remove(car)

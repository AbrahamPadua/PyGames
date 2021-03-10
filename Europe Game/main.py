import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Europe Guessing Game")
image = "europe.gif"
screen.addshape(image)
turtle.shape(image)


def write(country: str, x: float, y: float, size: int):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x, y)
    text.write(f"{country}", align="center",
               font=("Arial", size, "bold"))


europe = pd.read_csv("Europe.csv")
guessed_countries = []
correct_list = europe.country.to_list()

while len(guessed_countries) != 50:
    country = screen.textinput(
        title=f"{len(guessed_countries)}/50 Guessed Countries", prompt="What's another Country's name").title()

    if country == "exit":
        missing_states = filter(
            lambda x: x not in guessed_countries, correct_list)
        new_csv = pd.DataFrame(missing_states)
        new_csv.to_csv("countries_to_learn.csv")

    if country in correct_list and country not in guessed_countries:
        correct = europe[europe.country == country]
        x = float(correct.x)
        y = float(correct.y)
        font_size = int(correct.font_size)
        write(country, x, y, font_size)
        guessed_countries.append(country)


turtle.mainloop()

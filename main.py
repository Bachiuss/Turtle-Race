import turtle
import random


is_race_on = False
screen = turtle.Screen()
screen.setup(500, 400)
user = screen.textinput("Make Your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-230, positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)


if user:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user:
                print(f"U Won! The {winning_color} turtle is the winner!")
            else:
                print(f"U Lost! the {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

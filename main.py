from turtle import Turtle, Screen
import random

on_race = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Haga su apuesta", prompt="Qué tortuga va ganar? Elige un color: ")
colors = ["red", "blue", "yellow", "purple", "green", "gray"]
position_y = [-50, -20, 10, 40, 70, 100]
all_turtles = []
#6 tortugas
#posicion izquierda
for turtle in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(-230, position_y[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    on_race = True

while on_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            on_race = False
        rand_distance = random.randint(0, 11)
        turtle.forward(rand_distance)
        if turtle.pos(230):
            on_race = False
        elif user_bet == turtle.color()



















screen.exitonclick()
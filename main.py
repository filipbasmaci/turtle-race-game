from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet!", prompt="""Which turtle will win the race? Enter a color: 
(red, blue, yellow, green, orange)""")

print(f"You bet on {user_bet}")

all_turtles = []

red_turtle = Turtle(shape="turtle")
red_turtle.color("red")
red_turtle.penup()
red_turtle.goto(-230, 100)
all_turtles.append(red_turtle)

blue_turtle = Turtle(shape="turtle")
blue_turtle.color("blue")
blue_turtle.penup()
blue_turtle.goto(-230, 50)
all_turtles.append(blue_turtle)

yellow_turtle = Turtle(shape="turtle")
yellow_turtle.color("gold")
yellow_turtle.pencolor("yellow")
yellow_turtle.penup()
yellow_turtle.goto(-230, 0)
all_turtles.append(yellow_turtle)

green_turtle = Turtle(shape="turtle")
green_turtle.color("green")
green_turtle.penup()
green_turtle.goto(-230, -50)
all_turtles.append(green_turtle)


orange_turtle = Turtle(shape="turtle")
orange_turtle.color("orange")
orange_turtle.penup()
orange_turtle.goto(-230, -100)
all_turtles.append(orange_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} is the winner!")
            else:
                print(f"You lost! {winning_color} is the winner!")
        else:
            random_distance = random.randint(0,5)
            turtle.forward(random_distance)






screen.exitonclick()
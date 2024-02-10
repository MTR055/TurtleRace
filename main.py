from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=1000 , height=800)
my_screen.title("WELCOME TO TURTLE RACE")
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(-430,0)
tim.pencolor("brown")
tim.pensize(350)
tim.pendown()
tim.forward(860)
tim.pencolor('black')
tim.pensize(5)
tim.penup()
tim.goto(-410, -160)
tim.left(90)
tim.pendown()
tim.forward(320)
tim.penup()
tim.goto(450,-160)
tim.pendown()
tim.forward(320)




colours = ['violet','blue', 'green','yellow' ,'orange','red']

i=0
turtle_list = []
while i!=6:
    x = Turtle(shape="turtle")
    x.color(colours[i])
    x.penup()
    x.goto(-430, -150+60*i)
    turtle_list.append(x)
    i+=1

user_bet = my_screen.textinput(title="Make your input",prompt=" Which colour turtle will the race?")
print(user_bet)

if user_bet:
     is_game_on= True


while is_game_on:
    for turtle in turtle_list:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() >=430 :
            is_game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("you won")
            else:
                print("you lose")

my_screen.exitonclick()


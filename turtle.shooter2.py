import turtle
import random
import numpy as np
import pandas as pd
import mysql.connector 

range_list_1 = list(range(2,402,4))

list2 = []


def main_function():
    # start position 
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle1.speed(0)
    turtle2.speed(0)
    turtle1.up()
    turtle2.up()
    turtle1.goto(-200,0)
    turtle2.goto(200,0)
    turtle2.left(180)

    # there will be 100 rounds for each player 
    for i in range(100): 
        # They will shoot before meeting in the center 
        if turtle1.distance((0,0)) != 0 and turtle2.distance((0,0)) != 0:
            # every time each player walks forward 2 units 
            turtle1.forward(2)
            # the probility of shooting 
            if random.random()<=(((range_list_1[i])/400))**6:
                # shooting will change the color of turtle to yellow 
                turtle1.color("yellow")
                # when player 1 shoot and hit 
                if random.random()<=(range_list_1[i])/400:
                    Status = 'turtle 1 win'
                    list2.append(Status)
                    break
                # when player 2 shoot and miss 
                else:
                    Status = 'turtle 2 win'
                    list2.append(Status)
                    break
            turtle2.forward(2)
            if i == 50:
                turtle2.color("red")
                if random.random()<=0.5:
                    Status = 'turtle 2 win'
                    list2.append(Status)
                    break
                else:
                    Status = 'turtle 1 win'
                    list2.append(Status)
                    break

for j in range(30):
    main_function()
print(list2)
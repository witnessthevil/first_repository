import turtle
import random
import numpy as np
import pandas as pd
import mysql.connector 

range_list_1 = list(range(2,402,4))
range_list_2 = list(range(4,404,4))

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
            if random.random()<=(((range_list_1[i])/400))**7:
                # shooting will change the color of turtle to yellow 
                turtle1.color("yellow")
                # when player 1 shoot and hit 
                if random.random()<=(range_list_1[i])/400:
                    shooting = 'turtle 1 shoot'
                    Status = 'turtle 1 win'
                    distance = str(400 - range_list_1[i])
                    list2.extend([shooting,Status,distance])
                    break
                # when player 2 shoot and miss 
                else:
                    shooting = 'turtle 1 shoot'
                    Status = 'turtle 2 win'
                    distance = str(400 - range_list_1[i])
                    list2.extend([shooting,Status,distance])
                    break
            turtle2.forward(2)
            if random.random()<=(((range_list_2[i])/400))**7:
                turtle2.color("red")
                if random.random()<=((range_list_2[i])/400):
                    shooting = 'turtle 2 shoot'
                    Status = 'turtle 2 win'
                    distance = str(400 - range_list_2[i])
                    list2.extend([shooting,Status,distance])
                    break
                else:
                    shooting = 'turtle 2 shoot'
                    Status = 'turtle 1 win'
                    distance = str(400 - range_list_2[i])
                    list2.extend([shooting,Status,distance])
                    break
        



if __name__ == "__main__":
    for i in range(500):
        main_function()
    list3 = []
    split = np.array_split(list2,500)
    for data in split:
        if data[0][:9] == data[1][0:9]:
            data = np.append(data,"same")
        else:
            data = np.append(data,"diff")
        list3.append(data)
    connection = mysql.connector.connect(host='localhost',username='root',password='uttalogical99',database='final_project_honmono')
    cursor = connection.cursor()
    for i in list3:
        sql = """insert into battle_2 value(%s,%s,%s,%s)"""
        shoot = str(i[0])
        win = str(i[1])
        distance = int(i[2])
        diff = str(i[3])
        cursor.execute(sql,(shoot,win,distance,diff))
        connection.commit()


turtle.done()
        



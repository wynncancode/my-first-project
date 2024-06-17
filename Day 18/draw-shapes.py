## draw shapes from 3 sides to 10 sides polygon

from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("arrow")
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for sides in range (3,11):
    angle = 360 / sides
    tim.color(random.choice(colors))
    for shape in range(0,sides):
        tim.forward(100)
        tim.right(angle)










screen = Screen()
screen.exitonclick()
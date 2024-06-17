########### Draw a Colorful Dots Painting ########

import turtle as t
import random
#import colorgram

# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

t.colormode(255)
color_list = [(224, 58, 148), (198, 38, 125), (251, 215, 231), (232, 114, 171), (210, 6, 105), (237, 163, 198), (245, 242, 241), (242, 245, 244), (244, 132, 121), (253, 152, 151), (243, 244, 247), (44, 21, 33), (35, 22, 19), (110, 88, 84), (31, 30, 36), (35, 41, 37), (173, 109, 104), (82, 55, 52), (88, 86, 94), (158, 155, 162), (82, 86, 83), (62, 60, 70), (67, 65, 57), (59, 67, 62), (255, 1, 121), (131, 130, 121), (132, 136, 132), (193, 186, 200), (196, 193, 185)]

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













screen = t.Screen()
screen.exitonclick()
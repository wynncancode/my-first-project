from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_cc():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_cw():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_cc)
screen.onkey(key="d", fun=move_cw)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

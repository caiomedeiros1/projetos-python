from turtle import Turtle
import random

def get_color_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def car_coordinates():
    x_cor = random.randint(-310, 310)
    y_cor = random.randint(-210, 230)
    return (x_cor, y_cor)

class Car (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(get_color_tuple())
        self.penup()
        self.goto(car_coordinates())
        self.movespeed = random.randint(1, 3)
    
    def move(self):
        self.goto(self.xcor()-self.movespeed, self.ycor())

    def reset_position(self):
        self.goto(400, self.ycor())
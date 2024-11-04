from turtle import Turtle
import random

directions = [0, 180]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.locked = True
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        self.y_move *= -1
    
    def bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.bounce_paddle()
        self.goto(0, 0)
        self.locked = True
    
    def unlock_ball(self):
        self.locked = False
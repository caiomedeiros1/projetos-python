from turtle import Turtle

class Player (Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.goto(0, -250)
        self.shape("turtle")
        self.setheading(90)

    def walk(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def backwards(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
    
    def reset_position(self):
        self.goto(0, -250)
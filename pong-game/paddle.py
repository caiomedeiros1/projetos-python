from turtle import Turtle

STARTING_POSITION1 = (-350, 0)
STARTING_POSITION2 = (350, 0)

class Paddle(Turtle):
    def __init__ (self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        if player == 1:
            self.goto(STARTING_POSITION1)
        elif player == 2:
            self.goto(STARTING_POSITION2)
    
    def moveup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def moveup_press(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    
    def movedown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    
    def movedown_press(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
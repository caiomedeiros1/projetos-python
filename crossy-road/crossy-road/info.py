from turtle import Turtle

class Info (Turtle):
    def __init__ (self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"LEVEL: {self.level}", align="left", font=("Arial", 12, "bold"))
    
    def complete_level(self):
        self.level += 1
        self.update_score()
    
    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=("Arial", 12, "bold"))
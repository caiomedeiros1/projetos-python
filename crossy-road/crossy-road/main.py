from turtle import Screen
from player import Player
from car import Car
from info import Info
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
cars = []
num_cars = 10
info = Info()

screen.onkey(player.walk, "Up")
screen.onkey(player.backwards, "Down")
screen.listen()

game_is_on = True
new_level = True

while game_is_on:
    #Generate cars
    if new_level:
        for i in range(num_cars):
            new_car = Car()
            cars.append(new_car)
        new_level = False
    
    #Detect complete level 
    if player.ycor() >= 230:
        info.complete_level()
        player.reset_position()
        new_level = True

    #Set cars to move and reset their position
    for car in cars:
        if car.xcor() < -310:
            car.reset_position()

        #Detect collision with cars
        if (-20 < car.ycor() - player.ycor() < 20) and (-30 < car.xcor() - player.xcor() < 30):
            screen.onkey(None, "Up")
            screen.onkey(None, "Down")

            game_is_on = False
            
            while not game_is_on:
                info.game_over()
                screen.update()
                time.sleep(0.5)
                info.clear()
                info.update_score()
                screen.update()
                time.sleep(0.5)
        else:
            car.move()
    
    screen.update()
    time.sleep(0.01)
    

    

screen.exitonclick()
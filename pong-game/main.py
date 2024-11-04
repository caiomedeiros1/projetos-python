from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(1)
paddle2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle1.moveup, "w")
screen.onkeypress(paddle1.moveup_press, "w")
screen.onkey(paddle1.movedown, "s")
screen.onkeypress(paddle1.movedown_press, "s")

screen.onkey(paddle2.moveup, "Up")
screen.onkeypress(paddle2.moveup_press, "Up")
screen.onkey(paddle2.movedown, "Down")
screen.onkeypress(paddle2.movedown_press, "Down")

screen.onkey(ball.unlock_ball, "space")

screen.listen()

game_is_on = True 
time_control = 0.05

while game_is_on:
    time.sleep(time_control)

    if not ball.locked:
        ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #Detect collision with paddles
    if (ball.distance(paddle1) < 50 and ball.xcor() < -320 and ball.x_move < 0) or (ball.distance(paddle2) < 50 and ball.xcor() > 320 and ball.x_move > 0):
        ball.bounce_paddle()
        time_control *= 0.9
        print(time_control)
    
    #Detect when player2 misses
    if ball.xcor() > 380:
        scoreboard.p1_point()
        ball.reset_position()
        time_control = 0.05
    
    #Detect when player1 misses
    if ball.xcor() < -380:
        scoreboard.p2_point()
        ball.reset_position()
        time_control = 0.05

    screen.update()



screen.exitonclick()
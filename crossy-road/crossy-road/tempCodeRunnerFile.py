#Detect collision with cars
        if (-20 < car.ycor() - player.ycor() < 20) and (-30 < car.xcor() - player.xcor() < 30):
            game_is_on = False
            while not game_is_on:
                info.game_over()
                time.sleep(1)
                info.clear()
        else:
            car.move()
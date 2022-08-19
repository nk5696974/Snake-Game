from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)        #size of screen
screen.bgcolor("black")                    #set background color of screen
screen.title("My Snake Game.")             #set title of window
screen.tracer(0)                          #tracer->off

snake = Snake()
food = Food()
scBoard = ScoreBoard()

screen.listen()                             #to take input from user to move snake
screen.onkey(fun=snake.up, key="Up")                #create method in snake class
screen.onkey(snake.down, "Down")            
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()      #see documentation
    time.sleep(0.1)
    snake.move()
    scBoard.update()
    #Detect collision with food.
    if snake.head.distance(food) <15:         # 15 is distance between snake and food if sanake
        food.refresh()                        # pass within 15 it will be consider collision.
        snake.extend()                       # if we want to to hit food by head so decrese 15.
        scBoard.updateScore()                                   
    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scBoard.gameover()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scBoard.gameover()

screen.exitonclick()

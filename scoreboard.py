from turtle import Turtle

FONT = ("Verdana",15, "normal")
AlIGNMENT = "center"

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.shape("square")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update()

        
    def update(self):
        self.write(arg=f"Score: {self.score}",align=AlIGNMENT, move=False, font=FONT)


    def updateScore(self):
        self.score +=1
        self.clear()
        self.update()


    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",align=AlIGNMENT, move=False, font=FONT)

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore= 0
        self.rscore= 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))

    def addl(self):
        self.lscore+= 1
        self.update()

    def addr(self):
        self.rscore+= 1
        self.update()

    def win(self):
        self.goto(0,0)
        if self.lscore==5:
            self.write("GAme Over\n Left Win", align="center", font=("courier", 80, "normal"))
        else:
            self.write("Right\n win", align="center", font=("courier", 80, "normal"))


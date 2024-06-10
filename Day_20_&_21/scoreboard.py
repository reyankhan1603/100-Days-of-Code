from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", False, align = "center", font = ("Arial", 24, "normal"))
        
    def updatescore(self):
        self.clear()
        self.score += 5
        self.write(f"Score: {self.score}", False, align = "center", font = ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align = "center", font = ("Arial", 24, "normal"))
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

with open(r"Udemy\100 Days of Python\Snake Game\data.txt", mode="r") as data:
    data_score = int(data.read())

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"Udemy\100 Days of Python\Snake Game\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"Udemy\100 Days of Python\Snake Game\data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

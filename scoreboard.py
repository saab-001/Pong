from turtle import Turtle
from screen_designer import HEIGHT, MARGIN, UI_COLOR

FONT_FAMILY = ("Arial", 40, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(UI_COLOR)
        self.goto(0, (HEIGHT/2)-(MARGIN - 10))
        self.score_p1 = 0
        self.score_p2 = 0

    def show_score(self):
        self.clear()
        self.pendown()
        self.write(f"{self.score_p1}\t{self.score_p2}", False, "center", FONT_FAMILY)

    def score_add_p1(self):
        self.score_p1 += 1
        self.show_score()

    def score_add_p2(self):
        self.score_p2 += 1
        self.show_score()

    def game_over(self, pl1, pl2):
        self.penup()
        self.goto(-5, 10)
        self.pendown()
        if self.score_p1 > self.score_p2:
            self.write(f"GAME OVER", False, "center", FONT_FAMILY)
            self.goto(-5, -50)
            self.write(f"{pl2} Wins", False, "center", FONT_FAMILY)
        if self.score_p2 > self.score_p1:
            self.write(f"GAME OVER", False, "center", FONT_FAMILY)
            self.goto(-5, -40)
            self.write(f"{pl1} wins", False, "center", FONT_FAMILY)

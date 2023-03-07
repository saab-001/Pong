from turtle import Turtle

UI_COLOR = "white"
WIDTH = 1050
HEIGHT = 600
MARGIN = 85


class ScreenMaker(Turtle):

    def __init__(self):
        super().__init__()
        self.color(UI_COLOR)
        self.hideturtle()
        self.speed(10)
        self.create_screen()

    def create_screen(self):

        # Create a rectangular perimeter
        self.penup()
        self.goto(0, HEIGHT/2)
        self.pensize(2)
        self.pendown()
        self.setheading(180)
        self.forward(WIDTH/2)
        self.setheading(270)
        self.forward(HEIGHT-5)
        self.setheading(0)
        self.forward(WIDTH-5)
        self.setheading(90)
        self.forward(HEIGHT-5)
        self.setheading(180)
        self.forward(WIDTH/2)

        # Create a Score area
        self.setheading(270)
        self.forward(MARGIN)
        self.setheading(0)
        self.penup()
        self.forward(WIDTH/2)
        self.pendown()
        self.setheading(180)
        self.forward(WIDTH-5)
        self.penup()
        self.goto(-5, HEIGHT/2 - MARGIN)

        # Create a Separator line at the half
        self.setheading(270)
        self.forward(5)
        self.pendown()
        while True:
            self.pensize(4)
            self.forward(17)
            self.penup()
            self.forward(10)
            self.pendown()
            if self.ycor() < -(HEIGHT/2 - 5):
                break

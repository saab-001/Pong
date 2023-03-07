from turtle import Turtle

PAD_YCOR = -30
XCOR = 505
PAD_UP_LIMIT = 145
PAD_DOWN_LIMIT = -225
MOVEMENT = 20

# P1 : right
# P2 : left


class Paddles:

    def __init__(self):
        self.p1 = Turtle("square")
        self.p2 = Turtle("square")
        self.create_paddle()

    def create_paddle(self):

        # Create Player1 paddle
        self.p1.resizemode("user")
        self.p1.shapesize(1, 6)
        self.p1.color("white")
        self.p1.penup()
        self.p1.setheading(90)
        self.p1.goto(XCOR, PAD_YCOR)

        # Create Player2 paddle
        self.p2.resizemode("user")
        self.p2.shapesize(1, 6)
        self.p2.color("white")
        self.p2.penup()
        self.p2.setheading(90)
        self.p2.goto(-(XCOR + 6), PAD_YCOR)

    def p1_move_up(self):
        if self.p1.ycor() > PAD_UP_LIMIT:
            return
        self.p1.setheading(90)
        self.p1.forward(MOVEMENT)

    def p1_move_down(self):
        if self.p1.ycor() < PAD_DOWN_LIMIT:
            return
        self.p1.setheading(270)
        self.p1.forward(MOVEMENT)

    def p2_move_up(self):
        if self.p2.ycor() > PAD_UP_LIMIT:
            return
        self.p2.setheading(90)
        self.p2.forward(MOVEMENT)

    def p2_move_down(self):
        if self.p2.ycor() < PAD_DOWN_LIMIT:
            return
        self.p2.setheading(270)
        self.p2.forward(MOVEMENT)

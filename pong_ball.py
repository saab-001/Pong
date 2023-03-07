import random
from turtle import Turtle

BALL_COLOR = "blue"
START_LOCATION = (-5, -30)


class PongBall(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.speed(10)
        self.start()
        self.move_speed = 60

    def start(self):
        self.move_speed = 100
        self.goto(START_LOCATION)
        self.setheading(random.randint(150, 175) or random.randint(185, 210))

    def move(self):
        self.forward(10)

    def bounce_p1(self):

        # Right paddle bounce
        if self.heading() == 180:
            self.setheading(0)
        elif self.heading() < 90:
            angle = 180 - self.heading()
            self.setheading(angle)
        elif self.heading() > 270:
            angle = 180 + (360 - self.heading())
            self.setheading(angle)

        self.move_speed -= self.move_speed/10

    def bounce_p2(self):

        # Left paddle bounce
        if self.heading() == 0:
            self.setheading(180)
        elif self.heading() < 180:
            angle = 180 - self.heading()
            self.setheading(angle)
        elif self.heading() > 180:
            angle = 540 - self.heading()
            self.setheading(angle)

        self.move_speed -= self.move_speed/10

    def wall_bounce(self):

        # Upper wall bounce
        if self.heading() == 90:
            self.setheading(90 + random.randint(1, 30))
        elif self.heading() > 90:
            angle = 360 - self.heading()
            self.setheading(angle)
        elif self.heading() < 90:
            angle = 360 - self.heading()
            self.setheading(angle)

        # lower wall bounce
        elif self.heading() == 270:
            self.setheading(270 + random.randint(1, 30))
        elif self.heading() > 180:
            angle = 360 - self.heading()
            self.setheading(angle)
        elif self.heading() > 270:
            angle = 360 - self.heading()
            self.setheading(angle)

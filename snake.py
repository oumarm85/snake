from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_body = []
        self.length = 0
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in range(3):
            self.add_segment()

    def add_segment(self):
        self.segment = Turtle()
        self.segment.shape("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.setx(self.segment.xcor() + self.length)
        self.snake_body.append(self.segment)
        self.length -= 20

    def extend(self):
        self.add_segment()

    def move(self):
        # move last segment of the snake body in the position of the segment just in front of it, and do this for
        # each segment of the body. Then move the first segment wherever. This allows the body of the snake follow head
        for seg_num in range(len(self.snake_body) - 1, 0, -1):  # eg (start=2, stop=0, step=-1)
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    # prevents the head going back on itself
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg_num in self.snake_body:
            seg_num.goto(1000, 1000)  # move the existing snake off-screen
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

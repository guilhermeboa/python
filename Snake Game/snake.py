from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_pos = [0, 0]
        self.create_snake()

    def create_snake(self):
        x = 0
        for _ in range(3):
            snake = Turtle(shape='square')
            snake.penup()
            snake.color('white')
            snake.setx(x)
            self.snake_body.append(snake)
            x -= 20

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            xcor = self.snake_body[part - 1].xcor()
            ycor = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(xcor, ycor)
        self.snake_body[0].forward(20)
        self.collision()

    def new_body(self):
        snake = Turtle(shape='square')
        snake.penup()
        snake.color('white')
        snake.goto(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(snake)
        self.snake_pos.append(0)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def collision(self):
        for pos in self.snake_pos:
            print(self.snake_pos)
            if self.snake_body[0].position() == self.snake_pos[pos]:
                return True
            elif self.snake_body[0].xcor() > 270 or self.snake_body[0].xcor() < -270:
                return True
            elif self.snake_body[0].ycor() > 270 or self.snake_body[0].ycor() < -270:
                return True


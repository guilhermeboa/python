from turtle import Turtle

N_SCORE = 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.n_score = N_SCORE

    def score(self):
        self.setposition(0, 250)
        self.write(arg=f"Score: {self.n_score}", move=False, align='center', font=('Arial', 30, 'normal'))

    def increase_score(self):
        self.n_score += 1
        self.clear()
        self.score()

    def game_over(self):
        self.__init__()
        self.setposition(0, 0)
        self.write(arg="GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))


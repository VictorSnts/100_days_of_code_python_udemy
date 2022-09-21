from turtle import Turtle
import random


class Pilula(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("green")
        self.speed("fastest")
        self.atualiza_posicao()

    def atualiza_posicao(self):
        """Atualiza a posicao da pilula"""
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

import time
from turtle import Turtle

POS_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
DIST_PADRAO = 20

DIREITA = 0
CIMA = 90
ESQUERDA = 180
BAIXO = 270


def cria_parte(posicao):
    parte = Turtle()
    parte.color("blue")
    parte.shape("circle")
    parte.penup()
    parte.goto(posicao)
    return parte


class Cobra:

    def __init__(self):
        self.corpo = []
        self.cria_cobra()
        self.cabeca = self.corpo[0]
        self.calda = self.corpo[-1]

    def cria_cobra(self):
        """Cria uma nova cobra"""
        for pos in POS_INICIAL:
            parte = cria_parte(pos)
            self.corpo.append(parte)

    def atualiza_tamanho(self):
        """Atualiza o tamanho da cobra quando a pilula é coletada"""
        nova_parte = cria_parte(self.calda.pos())
        self.corpo.append(nova_parte)

    def mover(self):
        """Move a cobra"""
        for part_num in range(len(self.corpo) - 1, 0, -1):
            novo_x = self.corpo[part_num - 1].xcor()
            novo_y = self.corpo[part_num - 1].ycor()
            self.corpo[part_num].goto(novo_x, novo_y)
        self.corpo[0].forward(DIST_PADRAO)
        return self.sem_colisao_paredes() and self.sem_colisao_cauda()

    def sem_colisao_paredes(self):
        """Verifica se houve colisao com as paredes"""
        colisao_x = self.cabeca.xcor() > 290 or self.cabeca.xcor() < -290
        colisao_y = self.cabeca.ycor() > 290 or self.cabeca.ycor() < -290
        if colisao_x or colisao_y:
            return False
        else:
            return True

    def sem_colisao_cauda(self):
        """Verifica se houve colisao com as paredes"""
        for part_num in range(len(self.corpo) - 1, 0, -1):
            parte = self.corpo[part_num]
            if self.cabeca.distance(parte) < 10:
                return False
        return True

    def direita(self):
        """Faz a cobra virar para a direita"""
        if self.cabeca.heading() != ESQUERDA:
            self.cabeca.seth(DIREITA)

    def cima(self):
        """Faz a cobra virar para cima"""
        if self.cabeca.heading() != BAIXO:
            self.cabeca.seth(CIMA)

    def esquerda(self):
        """Faz a cobra virar para a esquerda"""
        if self.cabeca.heading() != DIREITA:
            self.cabeca.seth(ESQUERDA)

    def baixo(self):
        """Faz a cobra virar para baixo"""
        if self.cabeca.heading() != CIMA:
            self.cabeca.seth(BAIXO)

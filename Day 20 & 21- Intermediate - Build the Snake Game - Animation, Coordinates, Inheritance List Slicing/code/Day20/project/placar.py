from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')


class Placar(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.penup()
        self.hideturtle()
        self.atualiza_pontuacao()

    def atualiza_pontuacao(self):
        """Atualiza a pontuacao quando a pilula é coletada"""
        self.clear()
        self.setpos(0, 270)
        self.write(f"Pontuação: {self.pontuacao}", True, align=ALIGN, font=FONT)
        self.pontuacao += 1

    def game_over(self):
        """Indica o fina; da execucao do jogo"""
        self.clear()
        self.setpos(0, 0)
        self.write(f"GAME OVER\nVoce fez {self.pontuacao} pontos!", True, align=ALIGN, font=FONT)


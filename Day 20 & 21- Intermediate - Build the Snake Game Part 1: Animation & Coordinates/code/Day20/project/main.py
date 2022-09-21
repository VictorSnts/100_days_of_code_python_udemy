import time
from turtle import Screen, Turtle
from cobra import Cobra
from pilula import Pilula
from placar import Placar


def screen_update():
    screen.update()
    time.sleep(0.1)


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# TODO1 - Criar o corpo da cobra
snake = Cobra()
pill = Pilula()
placar = Placar()


# TODO3 - Controlar a cobra
screen.listen()
screen.onkey(snake.cima, "Up")
screen.onkey(snake.baixo, "Down")
screen.onkey(snake.esquerda, "Left")
screen.onkey(snake.direita, "Right")

# TODO2 - Movimentar a cobra
while True:
    screen_update()
    # TODO6 - DETECTAR COLICAO COM A PAREDE
    # TODO7 - DETECTAR COLISAO OM A CALDA
    if snake.mover():
        # TODO4 - DETECTAR COLISAO COM A PILULA
        if pill.distance(snake.cabeca) < 20:
            placar.atualiza_pontuacao()
            # TODO5 - CRIAR UM PLACAR
            pill.atualiza_posicao()
            snake.atualiza_tamanho()
    else:
        placar.game_over()
        break

screen.exitonclick()


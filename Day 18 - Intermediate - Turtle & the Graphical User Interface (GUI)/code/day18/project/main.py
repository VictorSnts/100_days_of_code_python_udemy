import turtle as t
import random as r
import colorgram


def get_color():
    """Extrai as cores de um arquivo de imagem e retorna uma tupla com os valores rgb"""
    extract_colors = colorgram.extract("sp-no-3.jpg.png", 5)
    colors = []

    for color in extract_colors:
        tup_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors.append(tup_color)

    return colors[r.randint(0, len(colors) - 1)]


# Constante de distancia entre os pontos
DISTANCIA = 25


# Controle das coordenadas
coordenadas = {
    "x": {
        "inicio": -200.0,
        "fim": 200.0
    },
    "y": {
        "inicio": -200.0,
        "fim": 200.0
    },
    "atual": {
        "x": -200.0,
        "y": -200.0
    },
}


# Criando os objetos e ajustando-os
turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)  # Define o modo de cores para usar rgb ate 255
turtle.pen(pendown=False)  # Define a linha pen como invisivel
turtle.speed("fastest")  # Define a velocidade para Rapido
turtle.hideturtle()  # Esconde o cursor


def draw_line():
    """Desenha uma linha"""
    while turtle.position()[0] <= coordenadas["x"]["fim"]:
        turtle.dot(20, get_color())
        turtle.forward(DISTANCIA)
        coordenadas["atual"]["x"] += DISTANCIA


def draw():
    """Desenha a imagem"""
    while turtle.position()[1] <= coordenadas["y"]["fim"]:
        turtle.setx(coordenadas["x"]["inicio"])
        turtle.sety(coordenadas["atual"]["y"])
        draw_line()
        coordenadas["atual"]["y"] += DISTANCIA


draw()

screen.exitonclick()

import random
import turtle as t
from colors import get_color

t.colormode(255)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


turtle = t.Turtle()
turtle.shape("turtle")


# turtle.color(get_color())


def challenge_1():
    """Desafio 1 - Fazendo um quadrado na GUI"""
    for _ in range(4):
        turtle.right(90)
        turtle.forward(100)


def challenge_2():
    """Desafio 2 - Desenhar uma linha pontilhada"""
    for i in range(20):
        turtle.forward(5)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()


def challenge_3():
    """Desafio 3 - Desenhar um triangulo, quadrado, pentagono, hexagono, heptagono, octogono, eneagono e decagono
    sobrepostos em sequencia"""
    DIST = 100

    def draw(sides):
        angle = 360 / sides
        turtle.color(get_color())
        for _ in range(sides):
            turtle.forward(DIST)
            turtle.right(angle)

    for i in range(3, 11):
        draw(i)


def challenge_4():
    """Desafio 4 - Faca percorrer um caminho aleatorio"""
    DIST = 25
    DIRECTIONS = [0, 90, 180, 270]

    for _ in range(101):
        turtle.pensize(10)
        turtle.color(rand_color())
        turtle.forward(DIST)
        turtle.setheading(random.choice(DIRECTIONS))


def challenge_5():
    SIZE = 100

    def draw(gap):
        """Desenhar um espirógrafo"""
        turtle.speed("fastest")
        circles = int(360 / gap)
        for _ in range(circles + 1):
            turtle.color(rand_color())
            turtle.circle(SIZE)
            turtle.left(gap)

    draw(2)


challenge_4()

screen = t.Screen()
screen.exitonclick()

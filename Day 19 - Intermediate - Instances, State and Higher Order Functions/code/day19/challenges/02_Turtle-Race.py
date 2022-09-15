import turtle as t
import random

from colors import get_color


screen = t.Screen()
turtles = []
pos = {"x": -300, "y": -200}

for _ in range(8):
    turtle = t.Turtle()
    turtle.shape('turtle')
    turtle.penup()
    turtle.color(get_color())
    turtle.sety(pos["y"])
    turtle.setx(pos["x"])
    pos["y"] += 50
    turtle.pendown()
    turtles.append(turtle)


def correr():
    escolha = screen.textinput("Escolha uma Tartaruga!", "Informe a cor da tartaruga que voce deseja apostar: ")
    first_pos = t.Turtle()
    first_pos.hideturtle()
    while first_pos.pos()[0] <= 300:
        for turt in turtles:
            passo = random.randint(5, 100)
            turt.forward(passo)
            if turt.pos()[0] > first_pos.pos()[0]:
                first_pos = turt
    if escolha == first_pos.color()[0]:
        print(f"Voce ganhou a aposta. A ganhadora foi a {first_pos.color()[0]}")
    else:
        print(f"Voce errou. A ganhadora foi a {first_pos.color()[0]}")


correr()

screen.exitonclick()

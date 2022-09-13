from time import sleep
from turtle import Turtle, Screen

# # Criando um objeto
# lucas = Turtle()
# print(lucas)
#
# tela = Screen()
# # Acessando um atributo do objeto
# print(tela.canvwidth)
# # Utilizando um metodo do objeto
# lucas.shape('turtle')
# lucas.color('green')
#
#
# def move_100():
#     sleep(1)
#     for i in range(4):
#         lucas.forward(25)
#
#
# move_100()
# tela.exitonclick()


# Utilizando outras bibliotecas
from prettytable import PrettyTable

tabela = PrettyTable()

campos = ["Nome", "Sobrenome", "Idade"]
dados = [
    ["Elisangela", "Santos", 48],
    ["Edivaldo", "Santos", 47],
    ["Victor", "Santos", 22],
    ["Vinicius", "Santos", 21],
    ["Lucas", "Santos", 5],
]


tabela.field_names = campos
tabela.add_rows(dados)
tabela.align = 'l'

print(tabela.get_string())
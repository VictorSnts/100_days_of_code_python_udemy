# ########### DEBUGGING #####################

# # Describe Problem
# def my_function():
#     # for i in range(1, 20):  # Errado
#     for i in range(1, 21):  # Corrigido
#         if i == 20:
#             print("You got it")
#
#
# my_function()
# # Problema = A funcao Range omite o limite superior (20), por isso nao inclui o 20.

# # Reproduce the Bug
# from random import randint
# # dice_imgs = ["❶", "❷", "❸", "❹", " ❺", "❻"]  # Errado
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]  # Corrigido
# # dice_num = randint(1, 6)  # Errado
# dice_num = randint(0, 5)  # Corrigido
# print(dice_imgs[dice_num])
# # Problema 1 = na linha 17 a funcao randint() recebe o numero de 1 a 6, o que nao representa os incicies corretos para
# #   a lista dice_num.
# # Problema 2 = Existe um " "  no indice 4 da lista dice_num.

# # # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     # print("You are a millenial.")  # Errado
#     print("You are a millenial.")  # Corrigido
# elif year >= 1994:
# #   print("You are a Gen Z.")  # Errado
#     print("You are a Gen Z.")  # Corrigido
# # Problema 1 = O ano de 1994 esta sendo ignorado nas duas condicionais
# # Problema 2 = A identacao esta incorreta nos blocos if e else

# # Fix the Errors
# # age = input("How old are you?")  # Errado
# age = int(input("How old are you?"))  # Corrigido
# if age > 18:
#     # print("You can drive at age {age}.")  # Errado
#     print(f"You can drive at age {age}.")  # Errado
# # Problema 1 - esta faltando identacao no bloco if
# # problema 2 - Esta faltando fazer cast para integer na variavel age
# # Problema 3 = Esta faltando tornar a string em fstring no comando print

# # Print is Your Friend
# # pages = 0  # Nao Necesssario
# # word_per_page = 0  # Nao Necesssario
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))  # Errado
# word_per_page = int(input("Number of words per page: "))  # Corrigido
# total_words = pages * word_per_page
# print(total_words)
# # Problema 1 =  na linha 50 temos uma comparação para a variavel word_per_page, quando deveria ser uma definição
# # Problema 2 = nao é necessario termos uma redeclaracao das variaveis, portanto aas linhas 47 e 48 nao sao necessarias

# Use a Debugger
# def mutate(a_list):
#   # b_list = []  # Errado
#   # for item in a_list:  # Errado
#   #   new_item = item * 2  # Errado
#   # b_list.append(new_item)  # Errado
#   # print(b_list)  # Errado
#     b_list = []  # Corrigido
#     for item in a_list:  # Corrigido
#         new_item = item * 2  # Corrigido
#         b_list.append(new_item)  # Corrigido
#     print(b_list)  # Corrigido
#
#
# mutate([1, 2, 3, 5, 8, 13])
# # Problema 1 - A identaçao do bloco da funcao estava incorreto
# # Problema 2 - A inclusao do item na b_list deve ocorrer dentro do laco for



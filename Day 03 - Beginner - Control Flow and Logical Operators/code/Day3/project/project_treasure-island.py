print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo a ilha do tesouro.")
print("Sua missão é encontar o tesouro perdido.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
encruzilhada = input("Você está em uma encruzilhada. Onde você quer ir? Digite \"esquerda\" ou \"direita\": ")

if encruzilhada.upper() == "ESQUERDA":
    lago = input("Você chegou a um lago. Há uma ilha no meio deste lago. "
                 "Digite \"esperar\" para esperar por um barco. "
                 "Digite \"nadar\" para tentar atravessar.")
    if lago.upper() == "ESPERAR":
        porta = input("Você chegou à ilha ileso. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. "
                      "Qual cor você escolhe?")
        if porta.upper() == "AMARELA":
            print("Voce encontrou tesouro. You Win")
        elif porta.upper() == "VERMELHA":
            print("Esta sala está completamente em chamas. Voce foi queimado pelo fogo. Game Over")
        elif porta.upper() == "AZUL":
            print("Esta sala é uma armadilha, esta cheia de bombas. Game Over")
        else:
            print("Game Over")
    else:
        print("Voce foi atacado por piranhas. Game Over")
else:
    print("Voce caiu em uma armadilha. Game Over")

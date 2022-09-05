import random
import hangman_words as hw
import hangman_art as ha

# Generate a random word from hangman_words.py
palavra_secreta = hw.get_word()
lifes = 6

# Print Hangman logo from hangman_art.py
print(ha.bem_vindo)
print(ha.stages[lifes])

# Generate as many blanks as letters in word
palavra_mascarada = []
for _ in palavra_secreta:
    palavra_mascarada.append("_")
print(palavra_mascarada)

# Ask the user to guess a letter
chutes_anteriores = []
# While all the blanks are not filled
while "_" in palavra_mascarada and lifes > 0:
    chute = input("\nChute uma letra: ")
    if chute in chutes_anteriores:
        print("Voce já chutou essa letra, tente uma outra.")
    else:
        chutes_anteriores.append(chute)

    # Check if the guessed letter is in the word
    # If it is True:
        if chute in palavra_secreta:
            #   Replace the blanks with the letter
            for posicao in range(len(palavra_secreta)):
                if chute == palavra_secreta[posicao]:
                    palavra_mascarada[posicao] = chute
        # If it is False:
        else:
            # Lose a live and print the hangman from hangman_art.py
            lifes -= 1
            # Tell the user the letter their chose is not in the word.
            print("A letra escolhida nao esta na palavra")
            # Check if they have more lifes
        print(palavra_mascarada)
        print(ha.stages[lifes])

if lifes <= 0:
    print("Voce nao tem mais vidas, Game Over")
    print(f"a palavra secreta era {palavra_secreta}")
else:
    print("Parabens! Voce ganhou!")
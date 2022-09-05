import random

# Step 3
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in chosen_word:
    display.append("_")

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#   letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    match = False
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
            match = True

    if match:
        print(display)
    else:
        print("Letter does not exist in the secret word!")

    if "_" not in display:
        end_game = True

print("You Won!")


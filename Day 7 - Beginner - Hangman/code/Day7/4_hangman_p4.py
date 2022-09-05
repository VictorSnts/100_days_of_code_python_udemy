import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Step 4
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
end_game = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Create blanks
display = []
for _ in chosen_word:
    display.append("_")

# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
#  remaining.
while not end_game:
    print(lives)
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    # Check guessed letter
    match = False
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
            match = True

    if match:
        print(display)
    else:
        print("Letter does not exist in the secret word!")
        lives -= 1

    if "_" not in display:
        end_game = True
        print("You Won!")







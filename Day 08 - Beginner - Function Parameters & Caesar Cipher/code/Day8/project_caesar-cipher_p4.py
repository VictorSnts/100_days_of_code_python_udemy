import art

# TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']


# TODO-3: What happens if the user enters a number/symbol/space?
#   Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#   e.g. start_text = "meet me at 3"
#   end_text = "•••• •• •• 3"
def input_validate(char):
    if char in numbers or char in symbols:
        return False
    elif char == " ":
        return False
    else:
        return True


def caesar(text_input, shift_input, direction_input):
    resultado = ""
    for pos in range(len(text_input)):
        if input_validate(text_input[pos]):
            index = alphabet.index(text_input[pos])
            # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
            #   Try running the program and entering a shift number of 45.
            #   Add some code so that the program continues to work even if the user enters a shift number greater
            #   than 26.
            #   Hint: Think about how you can use the modulus (%).
            if shift_input > len(alphabet):
                shift_input = shift_input % len(alphabet)
            if direction_input == "encode":
                try:
                    resultado += alphabet[index + shift_input]
                except IndexError:
                    nova_posicao = (index + shift_input) - len(alphabet)
                    resultado += alphabet[nova_posicao]
            elif direction == "decode":
                try:
                    resultado += alphabet[index - shift_input]
                except IndexError:
                    nova_posicao = (index - shift_input) + len(alphabet)
                    resultado += alphabet[nova_posicao]
            else:
                print("Invalid Option!")
                return
        else:
            resultado += text_input[pos]
    print(f"The {direction_input}d text is {resultado}")
    pass


# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#   e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#   If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#   Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
execute = True
while execute:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text_input=text, shift_input=shift, direction_input=direction)

    rerun = input("\n\nYou want to restart the cipher program? Yes or No? ").lower()
    if rerun == "no":
        execute = False



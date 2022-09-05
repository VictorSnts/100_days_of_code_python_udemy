alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_input, shift_input):
    resultado_encrypt = ""
    for pos in range(len(text_input)):
        if text_input[pos] != " ":
            index = alphabet.index(text_input[pos])
            try:
                resultado_encrypt += alphabet[index + shift_input]
            except IndexError:
                nova_posicao = (index + shift_input) - len(alphabet)
                resultado_encrypt += alphabet[nova_posicao]
        else:
            resultado_encrypt += " "
    print(f"The encoded text is {resultado_encrypt}")


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#   amount and print the decrypted text.
def decrypt(text_input, shift_input):
    resultado_decrypt = ""
    for pos in range(len(text_input)):
        if text_input[pos] != " ":
            index = alphabet.index(text_input[pos])
            try:
                resultado_decrypt += alphabet[index - shift_input]
            except IndexError:
                nova_posicao = (index - shift_input) + len(alphabet)
                resultado_decrypt += alphabet[nova_posicao]
        else:
            resultado_decrypt += " "
    print(f"The decoded text is {resultado_decrypt}")


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#   Then call the correct function based on that 'drection' variable.
#   You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
    encrypt(text_input=text, shift_input=shift)
elif direction == "decode":
    decrypt(text_input=text, shift_input=shift)
else:
    print("Invalid Option!")


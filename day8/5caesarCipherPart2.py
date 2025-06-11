alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called decrypt() that takes 'original_text'
#  and shift_amount as 2 inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text'
#  forwards in the alphabet by the shift_amount and print the decrypted text

def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {output_text}")

decrypt(text, shift)
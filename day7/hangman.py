word_list = ["aardvark", "baboon", "camel"]

# TODO 1: Randomly choose a word from word list and assign it to a variable
#  called chosen_word. then print it.

import random

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO 1.1: Create a placeholder with the same number of blanks as the chosen_word
placeholder = ""
for position in range(1, 6):
    placeholder += "_"
print(placeholder)

# TODO 2: Ask the user to guess a letter and assign their answer to a variable
#  called guess. Make guess lowercase

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter").lower()

    # TODO 3: Check if the letter the user guessed (guess) is one of the letters in
    #  the chosen_word. Print "Right" if it is, "Wrong" if it's not

    # TODO 3.1: Create a display that puts the guess letter in the right positions and _ in the rest of the string.

    display = ""
    for letter in chosen_word:
        if letter == guess:
            # print("Right") # TODO3
            display += letter #TODO3.1
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            # print("Wrong") # TODO3
            display += "_" #TODO3.1

    print(display)

    if "_" not in display:
        game_over = True
        print("You win")


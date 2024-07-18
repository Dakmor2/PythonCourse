#Step 2

import random
import re
import sys
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

word = []
lenght = len(chosen_word)
for i in range(0, lenght):
    word.append("_")
print(word)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Choose a letter\n").lower()
if not re.match("[a-z,A-Z]", guess):
    print("Error! Only letters a-z allowed!")
    sys.exit()
elif len(guess) > 1:
    print("Error! Only 1 letter allowed!")
    sys.exit()


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
word = []

for letter in chosen_word:
    if letter == guess:
        word.append(guess)
    else:
        word.append('_')
print(word)

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


import random
import re
import sys
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Choose a letter\n").lower()
if not re.match("[a-z,A-Z]", guess):
    print("Error! Only letters a-z allowed!")
    sys.exit()
elif len(guess) > 1:
    print("Error! Only 1 letter allowed!")
    sys.exit()
print(guess)
for letter in chosen_word: 
    if letter == guess:
        print("right")
    else:
        print("wrong")
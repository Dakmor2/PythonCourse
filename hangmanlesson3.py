import random
import re
import sys
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

underscore = "_"
position = ""
word = []
lenght = len(chosen_word)
for i in range(0, lenght):
    word.append("_")
print(word)

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
while underscore in word:
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
    

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            word[position] = guess
        
    print(word)
else:
    print("well done!")
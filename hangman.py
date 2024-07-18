import random
import sys
listwords = ["acqua", "aquilone", "soqquadro"]
randomword = random.choice(listwords)
print(randomword)
output = []
lives = 7
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
counter = 0
for i in range(len(randomword)):
    output.append("_")
print (f"Guess the word\n {output}")

while "_" in output:
    guess = (input("Insert a letter:\n")).lower()
    for n in range(len(randomword)):
        if guess == randomword[n]:
           output[n] = guess 
    if guess not in randomword:
       print(f"\n\nThe word doesn't have any {guess}.")
       lives -= 1
       print(HANGMANPICS[counter])
       counter += 1
       if lives == 0:
           print(f"\n\nThe word doesn't have any {guess}.")
           print(HANGMANPICS[6])
           print("GAME OVER")
           sys.exit()
    print(output)
else:
    print("Congratulations! You won!")
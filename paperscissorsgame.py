import random
playerchoice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
randompc = random.randint(0, 2)
if playerchoice == 0:
    print('''\n\n\n imagerock''')
elif playerchoice == 1:
    print('''\n\n\n imagepaper''')
elif playerchoice == 2:
    print('''\n\n\n imagescissors''')
if randompc == 0:
    print('''Computer chose:\n\n\n imagerock''')
elif randompc == 1:
    print('''Computer chose:\n\n\n imagepaper''')
elif randompc == 2:
    print('''Computer chose:\n\n\n imagescissors''')
if playerchoice == randompc:
    print("It's a draw")
elif playerchoice < randompc and not playerchoice == 0:
    print("You lose")
elif playerchoice > randompc and not randompc == 0:
    print("You win")
elif playerchoice == 0 and randompc == 2:
    print("you win")
elif randompc == 0 and playerchoice == 1:
    print("you win")
elif playerchoice == 0 and randompc == 1:
    print("you lose")
elif randompc == 0 and playerchoice == 2:
    print("you lose")



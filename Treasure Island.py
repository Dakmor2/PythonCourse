print("Welcome to Treasure Island, your mission is to find the treasure!")
choice1 = input("You are in front of a tunnel, you want to go left or right?\n").lower()
if choice1 == "left":
     choice2 = input("You end up in front of a lake. You want to wait for the boat or swim?\n").lower()
     if choice2 == "wait":
       choice3 = input("You end up in front of three doors. Which one you want to open? Red, Blue or Yellow one?\n").lower()
       if choice3 == "yellow":
            print("You've found the treasure!")            
       elif choice3 == "red":
            print("game over!")
       elif choice3 == "blue":
            print("game over!")
       else:
           print("game over!")
     elif choice2 == "secret":
         print("wow found the treasure!")      
     else:
        print("game over!")
elif choice1 == "secret":
    print("you found secret passage directly to the trasure. you won!")
else:
    print("game over!")

#     *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/______
# ******************************************************************************* ''')

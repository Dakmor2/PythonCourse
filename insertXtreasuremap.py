line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

positionline = int(position[1]) - 1
positioncolumn = position[0]

if positioncolumn == "B":
  positionx = 1
elif positioncolumn == "A":
  positionx = 0
elif positioncolumn == "C":
  positionx = 2

map[positionline][positionx] = "X"


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#alternative solution (easier)
#
#letter = position[0].lower()
#abc = ["a", "b", "c"]

#letter_index = abc.index(letter)  #give a number from a list
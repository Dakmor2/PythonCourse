# ticket machine for rollercoaster to sell ticket, check height 120 cm or more, age 12 5$, age 18 7$, more than 18 12$
print("Welcome to Rollercoaster ticket machine!")
height = int(input("Please insert your height: "))

#add if they want a photo for 3$
bill= 0
if height >= 120:
    age = int(input("Please insert your age: "))
    if age <= 12:
        print("The ticket for children is 5$.")
        bill = 5
    elif age <= 18:
        print("The ticket for young people is 7$.")
        bill = 7
    else: 
        print("The ticket for adults is 12$.")
        bill = 12
    wantspic = input("do you want a picture? Type Y or N: ")
    if wantspic == "Y":
        bill += 3
        print("Your bill is", bill)
    else:
        print("Your bill is", bill)
else:
    print("You are not tall enough for the rollercoaster.")
names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])

names = names_string.split(", ")
lenght = len(names)

import random
randomn = random.randint(0, lenght - 1)
randomperson = names[randomn]
print(f"{randomperson} is going to buy the meal today!")
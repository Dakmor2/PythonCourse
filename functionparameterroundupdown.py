# Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    numberscans = (height * width) / cover
    roundnumberscans = int(math.ceil(numberscans)) #round up numbers, for example 2.4 -> 3
    roundnumberscansdown = int(math.floor(numberscans)) #round down numbers, for example 2.8 -> 2
    roundnumberwithint = int(numberscans) #round number always down like math.floor
    print(f"You'll need {roundnumberscans} cans of paint.")
    print(roundnumberscansdown)
    print(roundnumberwithint)



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
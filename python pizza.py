print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

bill = 0

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  elif size != "S":
    bill += 3
else: bill = bill

if extra_cheese == "Y":
    bill += 1
else: bill = bill

if size == "S":
    bill += 15 
    print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill += 20
    print(f"Your final bill is: ${bill}.")
elif size == "L":
    bill += 25
    print(f"Your final bill is: ${bill}.")

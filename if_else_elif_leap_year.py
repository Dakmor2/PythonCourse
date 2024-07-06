# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

remainder4 = year % 4
remainder100 = year % 100
remainder400 = year % 400 

if remainder4 == 0:
  if remainder100 != 0:
    print("Leap year")
  elif remainder100 == 0:
    if remainder400 != 0:
      print("Not leap year")
    else:
      print("Leap year")
else:
  print("Not leap year")
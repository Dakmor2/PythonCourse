print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

# --------------------------
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1l = name1.lower()
name2l = name2.lower()
x = str(name1l.count("t") + name2l.count("t") + name1l.count("r") + name2l.count("r") + name1l.count("u") + name2l.count("u") + name1l.count("e") + name2l.count("e"))
y = str(name1l.count("l") + name2l.count("l") + name1l.count("o") + name2l.count("o") + name1l.count("v") + name2l.count("v") + name1l.count("e") + name2l.count("e"))
z = int(x + y)
if z < 10 or z > 90:
    print(f"Your score is {z}, you go together like coke and mentos.")
elif z >= 40 and z <= 50:
    print(f"Your score is {z}, you are alright together.")
else:
    print(f"Your score is {z}.")

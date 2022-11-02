# If statements = a block of code that will execute only if its condition is true
#
age = int(input("How old are you?: "))


if age == 100:
     print("You're really old, damn!")
elif age >= 18:
     print("You're an adult!")
elif age < 0:
     print("You're not even born yet!")
else:
     print("You're a child!")
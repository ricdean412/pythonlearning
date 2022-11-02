# Math Functions - Import Math
import math

# pi = -3.14
# x = 1
# y = 2
# z = 3


# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))

# Narcissistic Values:
def narcissistic( value ):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i) ** size
    return sum == int(value)
print(narcissistic(153)) #enter any amount here to check if narcisstic



# The == (Equal To) operator used to compare the
# values of two objects and The "is" operator compares
# the identity of two objects.

listOne = [20, 40, 60, 80]
listTwo = [20, 40, 60, 80]

print(listOne == listTwo)
print(listOne is listTwo)



# If you define a variable with the same name
# inside the function and global scope, a function
# will refer to the local variable by default.

salary = 8000
def printSalary():
    salary = 12000
    print("Salary:", salary)
printSalary()
print("Salary:", salary)

# We cannot use float numbers in range() function.
# Please refer to How to generate a range of float numbers.
for x in range(0.5, 5.5, 0.5):
  print(x)


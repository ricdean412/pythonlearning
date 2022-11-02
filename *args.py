# *args = parameter that will pack all arguements
#             into a tuple. useful so function can accept a varying
#             amount of arguements.

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[1] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,6))
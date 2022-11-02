# for loop = a statement that will execute
#             it's block of code a
#            limited amount of time
#
#                 while loop = unlimited
#                    for loop = limited


# ---------------
# Write a loop starting at 4 printing out every 3rd number sipping multiples of 3,
# ending at 16!

for i in range(4,17,3):
    if i % 3 != 0:
        print(i)


import time

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
#     print(i)

# for i in "Ric Dean":
#     print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Sup Brother!")



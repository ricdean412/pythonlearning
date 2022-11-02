#lists - used to store multiple items
#           in a single variable

food = ["pizza","ice cream","hot dogs","cheesesteaks","pudding"]

food[1] = "sushi"

# food.append("iphone")
# food.remove("hot dogs")
# food.pop()
# food.insert(1,"cake")
# food.sort()
# food.clear()

for x in food:
    print(x)


# The append() method appends an item to the end of the list
# . Therefore, we cannot pass the index number to it.
sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)
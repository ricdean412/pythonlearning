try:
    with open("/Users/ricsmacbook/Desktop/test.rf") as file:
        print(file.read())
except FileNotFoundError:
    print("The file wasn't found!")

print(file.closed)
# nested loops = The Inner loop will finish all of
#                It's iterations before finishing
#               one iteration of the "outer loops"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

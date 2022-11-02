#tuple = collection which is ordered and unchangeable
#           used to group together related data

student = ("Ric",23,"male")

print(student.count("Ric"))
print(student.index("male"))

for x in student:
    print(x)

if ["Ric",21] in student:
    print("Ric is 23 and a male.")
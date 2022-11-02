# sort() method = used with lists
# sort() function = used with iterables
# ---------------------------------------
# students = ("Ric","Dean","Joe","Dom","Chris")
            # () tuple - [] lists
# students.sort(reverse=True) #only lists
# sorted_students = sorted(students,reverse=True) #tuple sort

# for i in sorted_students:
#     print(i)

# --------------------------------------------

students = [("Ric","A",23),
            ("Dean","C",32),
            ("Joe","A",21),
            ("Dom","B",20),
            ("Chris","D",22)]
age = lambda ages:ages[2]
# students.sort(key=age,reverse=True)
sorted_students = sorted(students,key=age)

for i in sorted_students:
    print(i)
# Zip(*iterables) = aggregate elements from two or more
# iterables (list, tuples, sets, etc.) creates a zip
# object with paired elements stored in tuples
# for each element

usernames = ["Ric", "Dean", "Mister"]
passwords = ("pass123", "h@lloworld", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = (zip(usernames,passwords,login_date))

print(type(users))

for i in users:
    print(i)

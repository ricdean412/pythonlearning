# # Slicing = create a substring by extracting elements from another string
# #           indexing[] or slice ()
# #             [start:stop:step]
#
# INDEXING
#
# name = "Ric Dean"
#
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[0:8:2]
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

#SLICING

website1 = "http://google.com"
website2 = "https://youtube.com"

slice1 = slice(7,-4,)
slice2 = slice(8,-4)

print(website1[slice1])
print(website2[slice2])
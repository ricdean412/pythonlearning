# scope - the region that a variable is recognized
#             a variable is only availble from inside
#             the region it is created. Global and local
#             can be created.


def display_name():
    name = "Dean"   # local scope (available only inside this function)
    print(name)

name = "Ric"    # global scope

display_name()
print(name)

# L.E.G.B. = Local, Enclosing, Global, Built-in
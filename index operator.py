#index operator [] = gives access to  a sequences
#       elements

name = "ric dean!"

# if(name[0].islower()):
#     name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]



print(first_name + last_name)
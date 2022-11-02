# str.format() = optional method that gives users
#                 more control when displaying output

# animal = "cow"
# item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {1}".format(animal,item)) #positional_arguement
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword arguement

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# {} - format field
# formatting - respectively


# name = "Ric"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number)) #comma
print("The number is {:b}".format(number)) #binary
print("The number is {:o}".format(number)) #octal
print("The number is {:x}".format(number)) #hexademcial
print("The number is {:e}".format(number)) #scientific notation
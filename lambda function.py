# lambda function - function written in 1 line
#         using lambda keyword. Accepts any
#         number of arguments but only has one
#         expression. Throw - away

# lambda paramters:expressions

# def double(x):
#     return x * 2
#
# print(double(5))

# or

double = lambda x:x * 2
multiply = lambda x,y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False

# print(add(5,6,7))
# print(full_name("Ric","Dean"))
# print(age_check(18))
print(double(5))
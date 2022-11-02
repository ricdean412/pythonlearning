# keyword arguements - arguements preceded by an
#                     identifier when we pass them
#                     to a function. The order of the
#                     arguements doesn't matter, unlike
#                     positional arguements, Python knowns
#                     the names of the arguements that our
#                     function receives

# positional arguement:
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

# keyword arguements:
hello(first="Ric",last="Dean",middle="Beast")
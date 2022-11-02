# Dictionary - changeable unordered collection of
#   unique key value pairs Fast because they use
#   hashing, allowing us to access a value quickly.

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})

# capitals.pop('China')
# capitals.clear()

# print(capitals['Russia'])
# print(capitals['Germany'])
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,valve in capitals.items():
    print(key,valve)

# ------------------------
# To turn lists into dictionaries
names =  ["Ric","Dean","Stano"]
grades = ["A","B","C"]

dictionary = dict(zip(names,grades))
print(dictionary)
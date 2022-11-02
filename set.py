# set = collection which is unordered, unindexed,. No duplicated

utensils = {"fork","knife","spoon"}
dishes = {"bowl","plate","cup","knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
print(utensils.intersection((dishes)))

# for x in dishes:
#     print(x)



# The set is an unordered data structure. Therefore,
# we cannot access/add/remove its elements by index number.
sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1, "Vicki")
print(sampleSet)
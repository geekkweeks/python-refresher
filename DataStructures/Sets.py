"""
Sets are similar to the lists but are unordered and cannot contain duplicates(Unique elements even any duplicates element)
Uses curcly brackets
"""

my_set = {1, 2,4,5,1,2,5}
print(my_set)
print(len(my_set))

for i in my_set:
    print(i)

# will remove value=5
my_set.discard(5)
print(my_set)
# will add new value = 20
my_set.add(20)
print(my_set)

# will remove all elements
my_set.clear()
print(my_set)

# add one more element
my_set.update([19,30])
print(my_set)
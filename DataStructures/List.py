"""
Lists are a collection of data. u can modify the data
"""

my_list = [90, 100, 200, 500, 200]
print(my_list[0])
print(my_list[0:3])

my_list.append(999)
print(my_list)

# value = 3 will be set to index 2
my_list.insert(2,3)
print(my_list)

#will remove value = 100
my_list.remove(100)
print(my_list)

# will remove by index
my_list.pop(1)
print(my_list)

#sorted list
my_list.sort()
print(my_list)

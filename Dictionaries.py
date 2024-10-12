"""
Key and Value
"""

employee_dictionary = {
    'id': 'CV90392',
    'name': 'Alfan',
    'department': 'IT'
}

employee_dictionary['married'] = True

for i in employee_dictionary:
    print(i)

for x, y in employee_dictionary.items():
    print(x, y)

print(employee_dictionary.get('name'))
print(employee_dictionary.get('department'))
print(employee_dictionary.get('id'))

# remove key
employee_dictionary.pop('id')
print(employee_dictionary)

# clear dictionary
# employee_dictionary.clear()
print(employee_dictionary)

#will remove variable. If print will return error name 'dictionary' is not defined
del employee_dictionary
# print(employee_dictionary)

user_one = {
    'name': 'alfan',
    'address': 'Jl kebangsaan'
}

user_two = user_one
# if user_two remove one of keys then will also remove in user_one
user_two.pop('address')
print(user_two)
print(user_one)

#use .copy() to avoid same address in memory when copy the dictionary
# if remove one of keys then the original won't be removed
res_one = {
    'id': '123',
    'name': 'alfan',
    'salary': 829303
}
res_two = res_one.copy()
print(res_one)
print(res_two)
res_two.pop('salary')
print(res_one)
print(res_two)
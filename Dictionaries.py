"""
Key and Value
"""

employee_dictionary = {
    'id': 'CV90392',
    'name': 'Alfan',
    'department': 'IT'
}

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
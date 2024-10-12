"""
Functions
"""

def my_first_function():
    print("hello world!!")

def who_am_i(name):
    print(f"your name is {name}!")

def print_full_name(firstName, lastName):
    print(f"{firstName} {lastName}")

def print_numbers(firstNumber, lastNumber):
    print(f"{firstNumber} {lastNumber}")

def multiply_numbers(a, b):
    return a * b

# call function
my_first_function()
who_am_i("Alfan")
print_full_name("Alfan", "Zahriyono")
print_numbers(firstNumber=20, lastNumber=30)
print(multiply_numbers(a=20, b=30))
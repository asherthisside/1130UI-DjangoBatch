# There are 15 movie names in a list. Write a program to create another list that has the names which start with 'A'
movies = ['Ajhds', 'Cckregeuti', 'Ariusdg', 'KGF', 'Jkjckwrksj', 'RRR', 'KGF', 'Bahubali', 'Avengers', 'Passengers', 'Avengers: Endgame', 'John Wick', 'Pacific Rim', 'Achbwrs', 'Ahweiufd']
names_with_a = []
for i in movies:
    if i.startswith('A'):
        # print(i)
        names_with_a.append(i)

# print(names_with_a)

# Functions - Block of code that gets exexcuted only when it is called. To create a function in python, we use 'def' keyword
# 2 types of function - Predefined functions(Built-in functions), and user-defined functions(That are defined by the user) 

def print_name(name):
    print(f"My Name is {name}") 

print_name("Ashish")
print_name("Shuaib")


def introduction():
    print("Hi, this is my Introduction. I am this and that. I work here and there ")
    
# introduction()

# Arguments - 
def abc(a, b):
    print(a + b)

def my_introduction(name, address, age):
    print(f"Hello, My name is {name}, I am {age} years old and I live in {address}")

my_introduction("Mohtasham", "Noida", 24)

def square(num):
    # print(num ** 2)
    return num ** 2

# print(square(9))

sqo10 = square(10)
print(f"The square of 10 is {sqo10}")

# print(f"The square of 9 is {sqo9}")
def add(a, b):
    """This is the function that takes two numbers and returns the sum of those two numbers"""
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add.__doc__)

# num1 = int(input("Enter a number\n"))
# num2 = int(input("Enter another number\n"))

# choice = int(input("Enter you choice. Press:\n1. For addition\n2. For Subtraction\n3. For Multiplication\n4. For Division\n"))

# if choice == 1:
#     print(f"Result: {add(num1, num2)}")

# elif choice == 2:
#     print(f"Result: {sub(num1, num2)}")

# elif choice == 3:
#     print(f"Result: {mul(num1, num2)}")

# elif choice == 4:
#     print(f"Result: {div(num1, num2)}")

# else:
#     print("Enter a valid choice")

# Function docstring 
# print(input.__doc__)



# lambda functions  
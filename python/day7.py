# Lambda functions - Anonymous functions 
# Syntax lambda arguments : return

def cubes(x):
    return x ** 3

print(cubes(3))

cubelambda = lambda a : a ** 3 

# cubeof4 = cubelambda(4)

# print(cubeof4)

print(cubelambda(4))
print(cubelambda(5))

# if 12 > 13:
#     print("Yes")
# else:
#     print("No")

# Syntax for shorthand if-else
# statement if condition else statement

# print("Yes") if 12 < 13 else print("No")

# x = int(input("Enter a number\n"))

# print("Go higher") if x <= 10 else print("Go lower")

x = [2, 5, 6, 76, 23, 45, 21, 78, 3, 56, 54, 55]

if 3 in x:
    print("Present")
else:
    print("Absent")

print("Present") if 3 in x else print("Absent")
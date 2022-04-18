# num1 = int(input("Enter a number\n"))
# num2 = int(input("Enter another number\n"))

# minimum = min(num1, num2)
# print(minimum)
hcf = 0

# for i in range(1, minimum+1):
#     # print(i)
#     if num1 % i == 0 and num2 % i == 0:
#         # print(f"Yes, {i} is a common factor of {num1} and {num2}")
#         hcf = i 

# print(f"HCF is {hcf}")

# for i in range(1, (min(num1, num2) + 1)):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i 

# print(f"The HCF of {num1} and {num2} is {hcf}")

def print_squares(n):
    ls = []
    print(f"Printing squares from 1 to {n}")
    for i in range(1, n + 1):
        ls.append(i ** 2)
    
    return ls 

print(print_squares(23))

def sqdict(n):
    dict = {}
    print(f"Printing squares from 1 to {n}")
    for i in range(1, n + 1):
        dict.update({i : i ** 2})

    return dict

print(sqdict(17))

def sqfunc(n):
    return n ** 2

# for i in range(1, 11):
#     print(sqfunc(i))


# for i in range(1, 11):
    # print(pow(i, 2))

def square(a):
    return sqfunc(a)

print(square(5))

# def print_abc():
#     print("abc")
#     print_abc()


# print_abc()

def print_num(c):
    print(c)
    if c >= 0:
        print_num(c - 1)

print_num(10)
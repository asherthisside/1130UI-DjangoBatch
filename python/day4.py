# Loops - (Iterative statements)
# while and for loop

# age = 1
# while age <= 18:   
#     print(f"You need to go to school, you are just {age} years old")
#     age += 1
# print("Loop is over now")   


# name = input("Enter a number")
# n = int(name)
# print(n, type(n))
# b = input("Enter 0 or 1\t")
# answer = bool(b)
# print(answer, type(answer))

# if answer:
#     print("You entered True")
# else: 
#     print("You entered False")

# n = 0
# f = bool(n)

# if f == True:
#     print("You are right")

# else:
#     print("You are wrong")


# nu = 1
# while nu <= 30:
#     if nu % 2 == 0:
#         pass
#     print(nu)
#     nu += 1

# i = 1
# while i in range(1, 34):
#     print(i)
#     i += 1
print("Now, the loop is over")

list_upto_50 = list(range(1, 51))
# print(list_upto_50)

# for i in list_upto_50:
#     print(i)


names = ["Ashish", "Ankur", "Akanksha", "Shuaib", "Saurabh", "Ashish"]

# for i in names:
#     print(i)

# for i in range(0, 5):
#     print(names[i])


# a = int(input("Enter a number\n"))
# b = int(input("Enter another number\n"))

# print(min(a, b))

# hcf = 1
# for i in range(1, (min(a, b) + 1)):
#     if a % i == 0 and b % i == 0:
#         hcf = i
    
# print(f"HCF of {a} and {b} is {hcf}")

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i, j)
#     print()

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end='')
    print()


# print(list(range(1, 31, 4)))

# print(list(range(10, 0, -1)))
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()




# Solution for q.7.
str1 = "Saurabh"
first = str1[0]
last = str1[-1]

middle_index = len(str1) // 2
middle_character = str1[middle_index]
# print(first + middle_character + last)
# print(str[-1])
 

def firstOrlast(a):
    if a[0] == a[-1]:
        return True
    else: 
        return False

# print(firstOrlast([10, 20, 10, 30, 10]))


abc = 7536
n = str(abc)
r = n[::-1]
# print(type (n))
# for i in r:
#     print(i, end=" ")


abc = "guyv875&^%*jgbf"
chars = 0
digits = 0
special_chars = 0
for i in abc:
    if i.isalpha():
        chars += 1

    elif i.isdigit():
        digits += 1

    else: 
        special_chars += 1

print(f"Alphabets: {chars} | Digits: {digits} | Special Characters: {special_chars} | Total: {len(abc)}")
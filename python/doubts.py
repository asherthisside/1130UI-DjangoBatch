# def add(a, b):
#     print(a + b)

# # add(20, 20)

# def mul(a, b):
#     return a * b

# # print(mul(10, 2))

# # Nested For-loop 

# string_two = "This is a class"
# # for i in string_two:
# #     print(i)

# listoffriends = ['ram', 'shyam', 'manu', 'tanu']
# listoffriends[2] = 'Haaris'

# # print(listoffriends)

# data = list(range(1, 101))
# # print(data)


# name = "This is my name"
# print(name[2:15:2])

# # list[start:end:step]
# print(data[20:0:-1])


# # Email Slicer 
# mail = "haaris@trainingbasket.in"

# mail = "shivkumarstudy0@gmail.com"

# mail = "PadhLeMohtasham@gmail.com"

# indexofattherate = mail.index('@')
# print(indexofattherate)
# username = mail[0:mail.index('@')]
# print(username)

# domain = mail[(mail.index('@') + 1):len(mail)]
# print(domain)
from sys import intern
from traceback import print_tb


ls = [12, 23 ,434, 65, 68, 89, 45 ,67 ,43, 57, 4]
# print(min(ls))
# print(max(ls))


def abc(a, b, c, d):
    print(a, b, c, d)


# abc("A", "B", "C", "D")

def not_sure(*s):
    print(*s)

# not_sure(1, 2, 3, 4, 5, 6, 7, 8)
# not_sure(*ls)



string = "This is a string. I am this and that. I live here"
def loud(func):
    def internal(x):
        # func(x)
        print(x.upper())

    return internal

def whisper(func):
    def internal(x):
        # func(x)
        print(x.lower())

    return internal

# @loud
@whisper
def speak(s):
    return s

print(speak(string))

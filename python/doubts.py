def add(a, b):
    print(a + b)

# add(20, 20)

def mul(a, b):
    return a * b

# print(mul(10, 2))

# Nested For-loop 

string_two = "This is a class"
# for i in string_two:
#     print(i)

listoffriends = ['ram', 'shyam', 'manu', 'tanu']
listoffriends[2] = 'Haaris'

# print(listoffriends)

data = list(range(1, 101))
# print(data)


name = "This is my name"
print(name[2:15:2])

# list[start:end:step]
print(data[20:0:-1])


# Email Slicer 
mail = "haaris@trainingbasket.in"

mail = "shivkumarstudy0@gmail.com"

mail = "PadhLeMohtasham@gmail.com"

indexofattherate = mail.index('@')
print(indexofattherate)
username = mail[0:mail.index('@')]
print(username)

domain = mail[(mail.index('@') + 1):len(mail)]
print(domain)
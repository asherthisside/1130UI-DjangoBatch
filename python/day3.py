# # Dictionary - A collection type data type in python which is ordered, indexed and mutable. In dictionary data is stored in keys and values pair 
# data = {
#     "name" : "Ashish", 
#     "class" : 12, 
#     "subjects" : ['Maths', 'Science', 'English']
#     }

# # print(data["subjects"][1])

# car = {
#     "brand" : "Lamborghini", 
#     "model" : "countache", 
#     "year" : 1980,
#     "rebuild_year" : 1980,
# }

# # print(car)
# # print(car["model"])
# # car["model"] = "Aventador"
# # print(car)

# # print(len(car))
# # print(car.get("brand"))
# # print(car.keys())
# # print(car.items())

# specs = {
#     "engine": "v12",
#     "Nos" : True
# }

# car.update(specs)

# car.update({"price": 12312312312})
# print(car)

# car.pop("brand")
# car.popitem()
# car.clear()
# del(car)
# print(car)
# print(type(data))


# Tuple - Collection type data type
fruits = ('apple', 'banana', 'cherry', 'apple')
# print(fruits, type(fruits))
# print("This is a tuple")
# print(fruits[0])

# fruits[0] = 'Apple'

# print(len(fruits))
# print(fruits.count('apple'))
# print(fruits.index('apple'))


# set theory 

st = {"green", "blue", "white", "blue", "green"}
# print(st)
# print("This is a set")
# print(st)

numbers = {11, 23, 41, 54}
# numbers[0] = 123
# print(numbers[0])


# operators - 
# Indentity operator (Is, Is not)

x = 234
y = 23

x = y
# print(x is not y)

# Membership operator (In, not in)

fruits = ['Banana', 'Apple', 'Cherry']
x = 'Banana'

# print(x in fruits)

# Control structure 
# Conditional statements and Loops 

# if(condition) {
#     statements 
# }

ax = 432

# if (ax > 2000) {
#     print("condition true")
# }
# else {
#     print("condition false")
# }  

if ax > 200 and ax == 432:
    print("Condition is True") 
else:
    print("Condition is False")

name = "Asher"

if name == "Haaris":
    print("Entry allowed")

elif name == "Shuaib":
    print("Access granted")

elif name == "Asher":
    print("Aa ja tu bhi")
    
else:
    print("Entry denied")
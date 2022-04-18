# Datatypes - > Boolean (True / False)
condition = True 
condition = False 
# print(type(condition))


# Type conversion 
str_num = "12"
# str_num = False
num = int(str_num)
# print(num, type(num))
fl = float(num)
# print(fl, type(fl))

marks = 23
bool_marks = bool(marks)
# str_marks = str(marks)
str_marks = str(marks)
# print("Ashish got " + str_marks + " Marks")


# List 
ls = [1, 2, 3, 4, 5, 6]
names = ["Ashish", "Shruti", "Mohtasham", "Kanhaiya", "Saurabh", "Shuaib", "Mohtasham", "Shivam", 34, 54, 76, True]
# print(type(ls))
# print(ls)
# print(ls[7])
print(names)

# len() function
# print(len(ls))
# print(ls[len(ls) - 1])

# Adding the elements
# names.append("Haaris")
# print(names)

# names.insert(4, "Akanksha")
# print(names)

# names.insert(0, "Shibna")
# print(names)

names2 = ["Noida", "Mumbai", "Bangalore"]
names.extend(names2)
print(names)

# Removing Elements
# names.pop()
# names.pop(5)
# print(names)

# names.remove("Mohtasham")
# print(names)

# names.clear()
# print(names)

# del(names)
# print(names)

counter = names.count("Mohtasham")
# names.reverse()

ls = [11, 23, 43, 56, 2, 45, 87, 99, 23, 14]
print(ls)
# ls.sort(reverse=True)
# ls.reverse()
# print(ls)
ls.remove(23)

# Cooying of lists 
ls2 = ls 

# ls2.pop()
# print(ls)
# print(ls2)


ls2 = ls.copy()
ls2.pop()
print(ls)


# Dictionary ? 
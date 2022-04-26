from functools import reduce

# Map, Filter and Reduce 

# Iterables - 
# Iterators - 

ls = [1, 2, 3, 4]

# def dbl(n):
#     return n * 2

# doubles = list(map(dbl, ls))
doubles = list(map(lambda x : x * 2, ls))
# print(doubles)


def cubes(x):
    return x ** 3

# cbs = list(map(cubes, ls))
cbs = list(map(lambda x : x ** 3, [2, 4, 6, 8]))
# print(cbs)


# Filter function
ls = [2, 4, 3, 6, 7, 1, 9, 13, 22, 44, 34, 45, 67]

def evn(x):
    return x % 2 == 0

# evens = list(filter(evn, ls))

evens = list(filter(lambda x : x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
# print(evens)

# Reduce function

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def add_values(a, b):
    return a + b 

# total = reduce(add_values, ls)

total  = reduce(lambda a, b : a + b, ls)
# print(total)


def more(a, b):
    if a > b:
        return a 
    else:
        return b 
maxima = reduce(lambda x, y : x if x > y else y, [2, 4, 3, 6, 79, 11, 9, 13, 22, 44, 34, 45, 67])
# print(maxima)


list_of_multiples = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

# even_multiples = list(filter(lambda x : x % 2 == 0, list_of_multiples))
# print(even_multiples)

# sum_of_multiples = reduce(lambda a, b : a + b, even_multiples)

# print(sum_of_multiples)

sum_of_multiples = reduce(lambda a, b : a + b, list(filter(lambda x : x % 2 == 0, list_of_multiples)))

print(sum_of_multiples)

# Q - Write a list comprehension to create a list of first 30 multiples of 7


# functions

def abc(a):
    if a == 0:
        return print
    else:
        return sum([2, 4])


# a = abc(6)

# print(a)


def executor(func):
    func()

# executor(myIntro)

# Decorators 

def progress(func):
    def internal():
        print("Execution starting in 3, 2, 1 ...")
        func()
        print("Execution complete")
    return internal

# abc = progress(myIntro)
# abc()

@progress
def myIntro():
    print("My name is This and that")

# myIntro()


# List comprehension 

myList = list(range(1, 51))
# print(myList, type(myList))

list_of_evens = []
for i in range(1, 51):
    if i % 2 == 0:
        list_of_evens.append(i)

# print(list_of_evens)

list2 = [x for x in range(1, 51)]

# print(list2)

list_of_squares = [i ** 2 for i in range(1, 11)]
# print(list_of_squares)

list_gte_30 = [i for i in range(1, 51) if i > 30]
# print(list_gte_30)

list_of_evens_2 = [i for i in range(1, 51) if i % 2 == 0]
# print(list_of_evens_2)


movies = ['Ajhds', 'Cckregeuti', 'Ariusdg', 'KGF', 'Jkjckwrksj', 'RRR', 'KGF', 'Bahubali', 'Avengers', 'Passengers', 'Avengers: Endgame', 'John Wick', 'Pacific Rim', 'Achbwrs', 'Ahweiufd']

ls = []
# for i in movies:
#     if i.startswith('A'):
#         ls.append(i)
# print(ls)

ls = [i for i in movies if i.startswith('A')]
print(ls)
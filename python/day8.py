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

myIntro()
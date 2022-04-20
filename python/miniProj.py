# Q - Create a decorator that calculates the time taken by a function to get executed
import time


def timer(func):
    def internal(a):
        old_time = time.time()
        func(a)
        new_time = time.time()
        print(f"Time taken is {round(new_time - old_time, 3)} seconds")

    return internal


@timer
def squares(n):
    for i in range(1, n + 1):
        print(f"The square of {i} is {i ** 2}")

# squares(50)

for i in range(1, 11):
    print(i)
    time.sleep(2)
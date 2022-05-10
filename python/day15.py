import random

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    tries_left = 5
    while user_guess != random_number and tries_left != 0:
        print(f"You have {tries_left} tries left")
        tries_left -= 1
        user_guess = int(input("Guess the Number\t"))
        if user_guess < random_number:
            print("It's too low. Go a little higher")

        elif user_guess > random_number:
            print("It's too high. Go a little lower")

    if tries_left <= 0:
        print("You lost")
    else:
        print(f"Congratulations! You guessed the number {random_number} correctly")

        
guess(50)
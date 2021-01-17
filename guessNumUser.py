import random

def guess(x):
    random_number = random.randint(1, abs(x))
    guess = 0
    while guess != random_number:
        guess = input(f"Guess a number between 1 and {x}: ")
        try:
            guess = int(guess)
        except:
            print("Not a valid command guess again.")
            continue
        if guess > random_number:
            print("Sorry guess again. Too high.")
        elif guess < random_number:
            print("Sorry guess again. Too low.")

    print(f"You win! You guessed the number {random_number} correctly")

guess(15)
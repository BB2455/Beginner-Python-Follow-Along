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

def computer_guess(x):
    low = 1
    high = abs(x)
    feedback = ''
    turns = 0
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(H) or too low(L), or correct(C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        turns += 1
    
    print(f"The computer guessed your number {guess} in {turns} turns!")

computer_guess(15)
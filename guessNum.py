import random
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
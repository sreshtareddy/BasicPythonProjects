import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!=random_number:
        guess = int(input(f"Guess the number between 1 and {x} :"))
        if guess < random_number :
            print("Guessed number is Low !")
        elif guess > random_number:
            print("Guessed number is High !")
    print(f"Yeah you guessed the correct number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback!='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"The guessed value is {guess} is either too high(h) or low(l) or correct(c), type in :".lower())
        if feedback == "l":
            low = guess + 1
        elif feedback == "h":
            high = guess - 1
        
    print(f"Yah, the guessed number is{guess}")

computer_guess(20)
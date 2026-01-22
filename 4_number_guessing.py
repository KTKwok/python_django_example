import random

max_number = 10
min_number = 1
max_attempts = 3
secret_number = random.randint(min_number, max_number)

if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!")
    print(f"I have selected a random number between {min_number} and {max_number}. You have {max_attempts} to guess it.")

    guess = int(input(f"Attempt 1: Please enter your guess: "))
    if guess == secret_number:
        print(f"Congratulations, you guessed the number {secret_number}!")
    else:
        if guess > secret_number:
            max_number = guess
        else:
            min_number = guess
        print(f"The number should be from {min_number} to {max_number}.")
        guess = int(input(f"Attempt 2: Please enter your guess: "))
        if guess == secret_number:
            print(f"Congratulations, you guessed the number {secret_number}!")
        else:
            if guess > secret_number:
                max_number = guess
            else:
                min_number = guess
            print(f"The number should be from {min_number} to {max_number}.")
            guess = int(input(f"Attempt 3: Please enter your guess: "))
            if guess == secret_number:
                print(f"Congratulations, you guessed the number {secret_number}!")
            else:
                if guess > secret_number:
                    max_number = guess
                else:
                    min_number = guess
                print(f"The number should be from {min_number} to {max_number}.")
                print(f"Game over, the number was {secret_number}.")

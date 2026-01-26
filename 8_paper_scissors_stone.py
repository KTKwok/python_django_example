import random

AVAILABLE_CHOICE = ["W", "Y", "O"]

def get_computer_choice():
    return random.choice(AVAILABLE_CHOICE)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"{user_choice}<->{computer_choice}: Draw"
    elif (user_choice, computer_choice) in [("O", "Y"), ("Y", "W"), ("W", "O")]:
            return f"{user_choice}->{computer_choice}: You Win"
    return f"{user_choice}<-{computer_choice}: Computer Win"

def main():
    print("Welcome to Paper Scissors Stone!")

    while True:
        user_choice = input(f"Please enter your choice {AVAILABLE_CHOICE}, Q for quit: ").upper()
        if user_choice == "Q":
            break
        if user_choice not in AVAILABLE_CHOICE:
            print(f"Invalid choice: {user_choice}")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer choice: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

    print("Thanks for playing! Bye Bye")

if __name__ == '__main__':
    main()
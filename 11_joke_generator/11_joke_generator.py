import random
FILENAME = 'jokes.txt'

def read_joke(filename):
    try:
        with open(filename, 'r') as f:
            jokes = f.readlines()
            return [j.strip() for j in jokes]
    except FileNotFoundError:
        return []

def write_joke(filename, joke):
    with open(filename, 'a') as f:
        f.write(f"{joke}\n")

def main():
    while True:
        print("Welcome to joke generator")
        print("1. Get a random joke")
        print("2. Add a new joke")
        print("3. Exit")

        choice = input("Choose an option(1,2,3): ")

        if choice == '1':
            jokes = read_joke(FILENAME)
            if jokes:
                print("Your joke is:", random.choice(jokes))
            else:
                print("No jokes yet")
            continue

        if choice == '2':
            new_joke = input("Add a new joke: ")
            write_joke(FILENAME, new_joke)
            print("Your new joke is added")
            continue

        if choice == '3':
            print("Goodbye")
            break

        print("Invalid choice, please try again")
    print("Thank you for playing")

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    while True:
        str_input = input("Enter a number from 1 - 10: ")

        if not str_input.isdigit():
            print("Error, please enter a number")
            continue

        num = int(str_input)

        if 1 <= num <= 10:
            break
        else:
            print("Invalid Input, pls enter 1-10")
    print("Valid Input")

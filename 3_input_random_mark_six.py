import random

tickets = int(input("Enter the number of tickets: "))

for i in range(0, tickets):
    num = random.sample(range(1,50), 6)
    print(sorted(num))

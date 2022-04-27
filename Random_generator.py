import random

def loop():
    init = input("Do you want to generate numbers(n) or quit(q): ")
    if init == "n" or "number" or "numbers":
        print("Generating random numbers")
        n = random.random()
        print(n)
        loop()
    elif init == "q" or "quit":
        exit()
    else:
        print("Invalid input try again:")
        loop()

loop()
# Number Guessing Game(Computer)

import random
print("Think of a number between 1 to 10 and computer will try to guess it!")
high = 10
low = 1


if low <= high:
        guess = random.randint(low, high)
        print(f"Computer's guess is {guess}")
while True:
        feedback = input("Is the guess is too high type (H), too Low type(L) or correct type(C)").strip().upper()
        if feedback == "C":
            print("Yay! Computer guess your number correctly!")
            break
        elif feedback == "H":
               high = guess - 1
               guess = random.randint(low, high)
               print("Computer guess is: ",guess)
        elif feedback == "L":
               low = guess + 1
               guess = random.randint(low, high)
               print("Computer guess is: ", guess)
        elif feedback not in ["H", "L", "C"]:
               print("Invalid Input")

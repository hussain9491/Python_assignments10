import random

def main():
    # Generate the secret number randomly between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # First user guess
    guess = int(input("Enter a guess: "))

    # Loop until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess
        guess = int(input("Enter a new number: "))

    # When the guess is correct
    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()

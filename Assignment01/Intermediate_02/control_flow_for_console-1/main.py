import random

# Constants
NUM_ROUNDS = 5

# Game Start
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Initialize score
score = 0
# Play NUM_ROUNDS rounds

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate random numbers
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Show your number
    print(f"Your number is {your_number}")
    # Get user guess (with input validation)
    guess = int(input("Do you think your number is higher or lower than the computer's?: ").lower())
    while guess != "higher" and guess != "lower":
        guess = input("Please enter either 'higher' or 'lower': ").lower()
    
    # Game logic
    if your_number == computer_number:
        correct = False  # Computer wins ties
    elif guess == "higher" and your_number > computer_number:
        correct = True
    elif guess == "lower" and your_number < computer_number:
        correct = True
    else:
        correct = False
    
    # Print result
    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    # Show score
    print(f"Your score is now {score}")
    print()  # Blank line to separate rounds

# After the game ends
print("Thanks for playing!")

# Extension 2: Ending messages
if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")

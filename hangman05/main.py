# Import the random module for selecting a random word
import random

# Define the visual stages of the hangman
HANGMAN_STAGES = [
    # Stage 0 (0 wrong guesses)
    """
    -----
    |   |
        |
        |
        |
        |
    --------
    """,
    # Stage 1 (1 wrong guess)
    """
    -----
    |   |
    O   |
        |
        |
        |
    --------
    """,
    # Stage 2 (2 wrong guesses)
    """
    -----
    |   |
    O   |
    |   |
        |
        |
    --------
    """,
    # Stage 3 (3 wrong guesses)
    """
    -----
    |   |
    O   |
   /|   |
        |
        |
    --------
    """,
    # Stage 4 (4 wrong guesses)
    """
    -----
    |   |
    O   |
   /|\\  |
        |
        |
    --------
    """,
    # Stage 5 (5 wrong guesses)
    """
    -----
    |   |
    O   |
   /|\\  |
    |   |
        |
    --------
    """,
    # Stage 6 (6 wrong guesses - game over)
    """
    -----
    |   |
    O   |
   /|\\  |
    |   |
   / \\ |
    --------
    """
]
# List of words for the game
WORDS = ["PYTHON", "PROGRAMMING", "COMPUTER", "SCIENCE", "ALGORITHM"]

def main():
    # Select a random word from the list and convert to uppercase
    selected_word = random.choice(WORDS).upper()
    # Create a set of unique letters in the word
    unique_letters = set(selected_word)
    # Initialize guessed letters set
    guessed_letters = set()
    # Maximum allowed incorrect guesses
    max_incorrect = 6
    # Current incorrect guess count
    incorrect_count = 0
    
    # Game loop continues until win or loss
    while incorrect_count < max_incorrect and not unique_letters.issubset(guessed_letters):
        # Display current hangman stage
        print(HANGMAN_STAGES[incorrect_count])
        # Create display word with guessed letters revealed
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in selected_word])
        print(f"\nCurrent word: {display_word}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}\n")
        
        # Get and validate user input
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed that letter!")
                else:
                    break
            else:
                print("Please enter a single letter!")
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in selected_word:
            print("Correct guess!")
        else:
            print("Incorrect guess!")
            incorrect_count += 1
    
    # Final result check
    if unique_letters.issubset(guessed_letters):
        print(f"\nCongratulations! You won! The word was: {selected_word}")
    else:
        print(HANGMAN_STAGES[incorrect_count])
        print(f"\nGame over! The word was: {selected_word}")

# Run the game if executed as main program
if __name__ == "__main__":
    main()







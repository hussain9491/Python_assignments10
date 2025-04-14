"""
Program: favorite_animal
------------------------
This program asks the user for their favorite animal and responds
with a message saying it's also the program's favorite animal.
"""

def main():
    # Ask the user for their favorite animal
    animal = input("What's your favorite animal? ")

    # Respond with a message using the user's input
    print(f"My favorite animal is also {animal}!")

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

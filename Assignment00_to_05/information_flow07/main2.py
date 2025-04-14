def greet(name):
    """
    Returns a greeting message with the user's name.
    """
    return "Greetings " + name + "!"

def main():
    # Get the user's name
    name = input("What's your name? ")
    
    # Call the greet function and print the result
    print(greet(name))

# Call the main function to start the program
if __name__ == '__main__':
    main()

def print_multiple(message: str, repeats: int):
    """
    This function prints the given message 'repeats' number of times.
    """
    for i in range(repeats):  # Loop repeats 'repeats' number of times
        print(message)  # Print the message each time

def main():
    message = input("Please type a message: ")  # Get message input from the user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the number of repeats
    print_multiple(message, repeats)  # Call the function to print the message

if __name__ == '__main__':
    main()

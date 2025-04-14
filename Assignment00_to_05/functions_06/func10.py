def print_ones_digit(num):
    """
    Prints the ones digit of the given number 'num'.
    Uses the modulo operator to find the last digit.
    """
    print("The ones digit is", num % 10)

def main():
    # Prompt the user for a number and convert it to an integer
    num = int(input("Enter a number: "))
    
    # Call the function to print the ones digit
    print_ones_digit(num)

# This block ensures the main function is called when the script runs
if __name__ == '__main__':
    main()

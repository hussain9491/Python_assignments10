"""
Program: add2numbers
--------------------
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")

    # Prompt and read the first number
    num1 = input("Enter first number: ")
    num1 = int(num1)

    # Prompt and read the second number
    num2 = input("Enter second number: ")
    num2 = int(num2)

    # Calculate the sum
    total = num1 + num2

    # Print the total sum
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

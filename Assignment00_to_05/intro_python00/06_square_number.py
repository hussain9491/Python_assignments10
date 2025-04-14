"""
Program: number_square
----------------------
This program asks the user for a number and prints its square.
"""

def main():
    # Prompt the user for a number
    num = float(input("Type a number to see its square: "))
    
    # Calculate and print the square of the number
    print(str(num) + " squared is " + str(num ** 2))

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

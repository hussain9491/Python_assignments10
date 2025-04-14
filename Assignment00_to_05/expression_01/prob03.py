"""
An example program with constants
"""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches in 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet
    inches: float = feet * INCHES_IN_FOOT  # Convert feet to inches
    print("That is", inches, "inches!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

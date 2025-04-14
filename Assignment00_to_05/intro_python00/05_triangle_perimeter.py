"""
Program: triangle_perimeter
---------------------------
This program prompts the user to enter the lengths of
the three sides of a triangle and calculates the perimeter.
"""

def main():
    # Get the 3 side lengths of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print out the perimeter
    print("The perimeter of the triangle is " + str(perimeter))

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

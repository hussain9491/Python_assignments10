def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Check if divisible by 4
        if year % 100 == 0:  # Check if divisible by 100
            if year % 400 == 0:  # Check if divisible by 400
                print("That's a leap year!")
            else:  # Divisible by 100 but not by 400
                print("That's not a leap year.")
        else:  # Divisible by 4 but not by 100
            print("That's a leap year!")
    else:  # Not divisible by 4
        print("That's not a leap year.")

# This provided line is required at the end of
# the Python file to call the main() function
if __name__ == '__main__':
    main()

MINIMUM_HEIGHT: int = 50  # Minimum height required to ride

def main():
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# This provided line is required at the end of
# the Python file to call the main() function
if __name__ == '__main__':
    main()

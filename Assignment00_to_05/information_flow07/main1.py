ADULT_AGE = 18  # The legal age of adulthood in the United States

def is_adult(age: int):
    """
    Returns True if the age is greater than or equal to the legal adult age (ADULT_AGE),
    otherwise returns False.
    """
    if age >= ADULT_AGE:
        return True
    return False

def main():
    # Ask the user for the age
    age = int(input("How old is this person?: "))
    
    # Print whether the person is an adult or not
    print(is_adult(age))

# Call the main function to start the program
if __name__ == "__main__":
    main()

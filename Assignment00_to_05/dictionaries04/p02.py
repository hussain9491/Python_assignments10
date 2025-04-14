def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # If name is empty, stop the input loop
            break
        number = input("Number: ")
        phonebook[name] = number  # Add the name and number to the phonebook

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")  # Print each name and number


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # If name is empty, stop the lookup loop
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            print(f"{name}'s number is {phonebook[name]}")


def main():
    phonebook = read_phone_numbers()  # Collect phonebook entries from user
    print_phonebook(phonebook)  # Print all entries in the phonebook
    lookup_numbers(phonebook)  # Allow the user to look up phone numbers


# Python boilerplate.
if __name__ == '__main__':
    main()

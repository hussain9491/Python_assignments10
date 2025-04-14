def count_even(lst):
    """
    Returns the number of even numbers in the list.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  # Initialize a counter for even numbers
    for num in lst:  # Loop through all the numbers in the list
        if num % 2 == 0:  # Check if the number is even
            count += 1  # Increase the counter if the number is even
    
    print(count)  # Print the total count of even numbers

def get_list_of_ints():
    """
    Reads integers from the user until they press enter and returns the resulting list.
    """
    lst = []  # Create an empty list to store the integers
    user_input = input("Enter an integer or press enter to stop: ")  # Get user input
    
    # Loop until the user presses enter without typing a number
    while user_input != "":
        lst.append(int(user_input))  # Add the input number to the list
        user_input = input("Enter an integer or press enter to stop: ")  # Get the next user input
    
    return lst  # Return the populated list

def main():
    lst = get_list_of_ints()  # Get the list of integers from the user
    count_even(lst)  # Count and print the even numbers in the list

# This part calls the main function when the program is run
if __name__ == '__main__':
    main()

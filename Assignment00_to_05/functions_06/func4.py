def double(num: int):
    """
    Returns the result of multiplying the input number by 2.
    """
    return num * 2

def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the double function to calculate the doubled value
    num_times_2 = double(num)
    
    # Print the result
    print("Double that is", num_times_2)

# This part calls the main function when the program is run
if __name__ == '__main__':
    main()

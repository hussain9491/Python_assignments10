def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # Continue doubling the number until it's 100 or greater
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2
        
        # Print the new value
        print(curr_value)

# Python boilerplate to run the main function
if __name__ == '__main__':
    main()

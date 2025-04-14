MAX_TERM_VALUE = 10000  # Set the maximum value for the Fibonacci sequence

def main():
    # Initialize the first two terms of the Fibonacci sequence
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    
    # Print Fibonacci numbers while the current term is less than or equal to MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        # Calculate the next Fibonacci number
        term_after_next = curr_term + next_term
        # Move to the next terms in the sequence
        curr_term = next_term
        next_term = term_after_next


# Python boilerplate to call the main function
if __name__ == '__main__':
    main()

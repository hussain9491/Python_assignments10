def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b.
    """
    total = a + b
    return total / 2

def main():
    # Example 1: Find the average of 0 and 10
    avg_1 = average(0, 10)
    # Example 2: Find the average of 8 and 10
    avg_2 = average(8, 10)
    
    # Find the average of the two previously calculated averages
    final = average(avg_1, avg_2)
    
    # Print the results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This is required to run the main function
if __name__ == '__main__':
    main()

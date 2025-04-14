def print_divisors(num: int):
    """
    This function prints all divisors of the given number.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):  # Loop through numbers from 1 to num
        if num % i == 0:  # Check if i is a divisor of num (no remainder)
            print(i)

def main():
    num = int(input("Enter a number: "))  # Prompt user to input a number
    print_divisors(num)  # Call the function to print divisors of the number

# This line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()

def main():
    # Loop through numbers from 10 to 19 (inclusive)
    for i in range(10, 20):
        # Print number followed by "even" or "odd"
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

# This provided line is required at the end of the file to call the main() function.
if __name__ == '__main__':
    main()

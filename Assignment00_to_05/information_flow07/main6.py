def subtract_seven(num):
    # Subtract 7 from the input number
    num = num - 7
    return num

def main():
    num = 7  # You can modify this number to test with other values
    num = subtract_seven(num)  # Call the helper function to subtract 7
    print("this should be zero: ", num)  # Print the result after subtraction

if __name__ == '__main__':
    main()

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if low <= n <= high:
        return True
    return False

def main():
    # Example usage
    print(in_range(5, 1, 10))  # True
    print(in_range(15, 1, 10))  # False
    print(in_range(10, 1, 10))  # True

if __name__ == '__main__':
    main()

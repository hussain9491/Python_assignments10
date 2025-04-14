import random

# Set the likelihood of the 'done' function returning True
DONE_LIKELIHOOD = 0.3  # Adjust this as necessary

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # End the function early if done() returns True
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Perform the counting
    print("I'm done")

if __name__ == "__main__":
    main()

"""
Program: friends_ages
---------------------
This program calculates and prints the ages of
Anton, Beth, Chen, Drew, and Ethan based on the given conditions.
"""

def main():
    # Anton's age is given
    anton = 21

    # Beth is 6 years older than Anton
    beth = anton + 6

    # Chen is 20 years older than Beth
    chen = beth + 20

    # Drew is as old as Chen's age plus Anton's age
    drew = chen + anton

    # Ethan is the same age as Chen
    ethan = chen

    # Print out all the ages
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

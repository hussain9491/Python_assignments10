def add_three_copies(my_list, data):
    # Add three copies of data into the list
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    # Ask the user to input a message
    message = input("Enter a message to copy: ")
    my_list = []  # Start with an empty list
    print("List before:", my_list)
    
    # Call the function to add three copies of the message
    add_three_copies(my_list, message)
    
    # Print the list after modification
    print("List after:", my_list)

# This provided line is required to call the main function.
if __name__ == "__main__":
    main()

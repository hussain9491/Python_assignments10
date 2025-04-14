def access_element(lst, index):
    # Access the element at the given index
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    # Modify the element at the given index
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    # Return a slice of the list
    if 0 <= start <= len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Start or end index out of range."

def main():
    # Initialize a list
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter 1, 2, 3, or 4: ")
        
        if choice == '1':
            idx = int(input("Enter index to access: "))
            result = access_element(my_list, idx)
            print("Result:", result)
        
        elif choice == '2':
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            result = modify_element(my_list, idx, new_val)
            print("Result:", result)
        
        elif choice == '3':
            start_idx = int(input("Enter start index: "))
            end_idx = int(input("Enter end index: "))
            result = slice_list(my_list, start_idx, end_idx)
            print("Sliced list:", result)
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

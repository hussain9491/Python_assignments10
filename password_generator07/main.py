# create  a password suggestion generator using python 

import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            # Get password length
            length = int(input("Enter the length of the password (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            
            # Get number of passwords
            num_passwords = int(input("How many passwords would you like to generate? "))
            if num_passwords < 1:
                print("Please enter a positive number.")
                continue
            
            # Generate and display passwords
            print("\nGenerated Passwords:")
            print("-" * 50)
            for i in range(num_passwords):
                password = generate_password(length)
                print(f"Password {i+1}: {password}")
            
            break
            
        except ValueError:
            print("Please enter valid numbers.")
        
        # Ask if user wants to generate more passwords
        choice = input("\nDo you want to generate more passwords? (yes/no): ").lower()
        if choice != 'yes':
            break
    
    print("\nThank you for using the Password Generator!")

if __name__ == "__main__":
    main() 

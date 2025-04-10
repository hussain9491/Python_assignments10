# created by me password generator suggestion in simple way 
# Assignment 07

import random
import string
print("Welcome to Your password suggestions generator! ")
chars = [string.ascii_letters, string.digits, string.punctuation]

user = int(input("Enter a amount of passwords you want!"))
userinput = int(input("How many characters do you want in your password? \n"))

print("here's your password suggestions:\n")

for i in range(user):
    password = ''.join (random.choice(''.join (chars))
    
         for x in range(userinput))
    print(password)
# create a number guessing game where the user has to guess a correct company name.

import random
guess_value = ["NIKE", "ADIDAS", "PUMA"]
print("Hey User! We play a game of guessing shoe company name\n ")
print("you have to guess the name of the shoe company, (nike, adidas, puma) \n")
while True:
    guess = input("Guess a shoe company name: ").upper()
    
    if random.choice(guess_value) in guess:
    
        print("You are correct, the shoe company name is " + guess)
        break
    elif guess not in guess_value:
        print("invalid input! guess one of the shoe company name (nike, adidas, puma)")
    
 
    else:
        print("Sorry, that is not correct. The shoe company name is not " + guess)


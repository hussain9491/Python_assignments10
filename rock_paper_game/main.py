# Rock Paper Scissor Game Computer vs User
import random
print("Welcome To The Rock Paper Scissor Game")
choices = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0
print("Let\'s Play😋")
while True: 
    user = input("Type Rock, Paper, Scissor or Q for Quit\n").lower()
    if user == "q":
        print("Thanks for playing, see you next time!")
        print(f"your score {user_score} and computer score is {computer_score}")
        
        break
    elif user  not in choices:
        print("Invalid Input. Please Try Again")
        continue
    computer_choose = random.choice(choices)
    print(f"Computer choose {computer_choose}")
    if user == computer_choose: 
        print(f"it's Tie!😅 you choose {user}, and computer choose {computer_choose}😅, play one more time🤔")
    elif (user == "rock" and computer_choose == "scissor") or \
    (user == "paper" and computer_choose == "rock") or \
    (user == "scissor" and computer_choose == "paper"):
        print("You Win the game! Congratulations!🤗")
        user_score += 1
    else:
        print("Computer Win hehehe😚")
        computer_score += 1
        if user_score == 5:
            print("You Win the game 5 times! you are now expert!😮")
            break



# Mad lib project  Assignment 01

print("lets play Mad Libs! fill in the Blanks with your own words")
def mad_lib():
    user_input = input("Enter Book Name\n")
    user_input2 = input("Enter Author Name\n")
    user_input3 = input("How many pages in this book?\n")
    user_input5 = input("Enter the name of the main character\n")
    user_input4 = input("Enter the price\n")
    result = f'''
this is a book called {user_input} written by {user_input2} it has {user_input3} pages and the main character is {user_input5} it costs {user_input4} dollars😅
'''
    print("Here is your Mad Libs story:👇🏻 \n\n",result)
    
mad_lib()
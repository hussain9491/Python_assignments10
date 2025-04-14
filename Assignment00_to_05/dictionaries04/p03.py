def main():
    # Dictionary containing the price of each fruit
    fruits = {
        'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5
    }
    
    total_cost = 0  # Initialize the total cost to 0
    
    # Loop through the fruits dictionary
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the fruit
        # Prompt the user for the number of fruits they want to buy
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))
        # Add the cost of the current fruit to the total cost
        total_cost += (price * amount_bought)
    
    # Print the total cost of all the fruits
    print(f"Your total is ${total_cost:.2f}")  # Display the total cost with 2 decimal places


# Python boilerplate
if __name__ == '__main__':
    main()

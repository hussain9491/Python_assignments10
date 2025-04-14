"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Gravity factors relative to Earth
    GRAVITY = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    try:
        # Ask the user for weight on Earth
        earth_weight = float(input("Enter a weight on Earth: "))
        
        # Ask the user for the planet
        planet = input("Enter a planet: ")
        
        # Calculate the equivalent weight
        equivalent_weight = earth_weight * GRAVITY[planet]
        
        # Round the result to 2 decimal places
        equivalent_weight = round(equivalent_weight, 2)
        
        # Print the result
        print(f"\nThe equivalent weight on {planet}: {equivalent_weight}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

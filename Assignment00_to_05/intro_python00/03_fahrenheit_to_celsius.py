"""
Program: fahrenheit_to_celsius
------------------------------
This program asks the user for a temperature in Fahrenheit
and converts it to Celsius using the proper formula.
"""

def main():
    # Prompt the user for temperature in Fahrenheit
    degrees_fahrenheit = input("Enter temperature in Fahrenheit: ")
    degrees_fahrenheit = float(degrees_fahrenheit)

    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Output the result
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()

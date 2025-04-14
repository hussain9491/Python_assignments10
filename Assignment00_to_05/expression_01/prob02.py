C: int = 299_792_458  # The speed of light in meters per second

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

import math  # Import math module to use math.sqrt()

def main():
    # Ask the user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Use the Pythagorean theorem: BC² = AB² + AC²
    bc = math.sqrt(ab**2 + ac**2)

    # Print the length of the hypotenuse
    print("The length of BC (the hypotenuse) is:", bc)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
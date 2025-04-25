def main():
    # Ask the user for the two numbers
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient and remainder
    quotient = num1 // num2
    remainder = num1 % num2

    # Display the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

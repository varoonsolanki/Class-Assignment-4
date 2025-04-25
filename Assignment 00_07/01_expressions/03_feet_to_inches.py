def main():
    # Ask the user to enter the number of feet
    feet = float(input("Enter the number of feet: "))

    # 1 foot = 12 inches
    inches = feet * 12

    # Display the result
    print(str(feet) + " feet is equal to " + str(inches) + " inches.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

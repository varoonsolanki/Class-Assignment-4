def main():
    # Prompt the user to enter a number
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number * number
    
    # Print the result
    print(f"{number} squared is {square}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

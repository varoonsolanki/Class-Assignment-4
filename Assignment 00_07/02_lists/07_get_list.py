def main():
    lst = []  # Initialize an empty list to store values

    val = input("Enter a value: ")  # Get the first value from the user
    while val:  # This loop runs until the user enters an empty string
        lst.append(val)  # Add the input value to the list
        val = input("Enter a value: ")  # Prompt the user for the next value

    print("Here's the list:", lst)  # Print the list when the loop ends


# This provided line is required to call the main function when the script runs
if __name__ == '__main__':
    main()

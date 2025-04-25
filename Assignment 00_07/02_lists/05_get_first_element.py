def get_first_element(lst):
    """
    Prints the first element of a provided list.
    Only if the list is not empty.
    """
    if lst:  # Check if the list is non-empty
        print(lst[0])  # Prints the first element of the list
    else:
        print("The list is empty!")  # Handle empty list case

# Helper function to gather a list of elements from user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Continue until the user presses enter without typing anything
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Main function that calls the helper functions
def main():
    lst = get_lst()  # Get the list from the user
    get_first_element(lst)  # Print the first element of the list

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()

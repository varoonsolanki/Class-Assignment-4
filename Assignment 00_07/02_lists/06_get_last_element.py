def get_last_element(lst):
    """ Prints the last element of the provided list if the list is not empty. """
    if lst:  # Check if the list is not empty
        print(lst[-1])  # Print the last element using negative indexing
    else:
        print("The list is empty.")  # Inform the user if the list is empty

# Helper function to gather a list of elements from user input
def get_lst():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Continue until the user presses enter without typing anything
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Main function that calls the helper functions
def main():
    lst = get_lst()  # Get the list from the user
    get_last_element(lst)  # Print the last element of the list

# This line ensures the main function runs when the script is executed
if __name__ == '__main__':
    main()

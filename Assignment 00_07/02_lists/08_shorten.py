MAX_LENGTH : int = 3

def shorten(lst):
    """Removes elements from the end of the list until the list has MAX_LENGTH elements."""
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Removes and returns the last element
        print(last_elem)  # Print the element that was removed

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":  # Loop until the user presses enter without typing anything
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from user input
    shorten(lst)  # Shorten the list by removing elements from the end

if __name__ == '__main__':
    main()

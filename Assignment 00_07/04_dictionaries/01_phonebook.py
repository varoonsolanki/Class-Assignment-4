def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":  # Break when user enters a blank line
            break
        
        # Check if the name already exists in the phonebook
        if name in phonebook:
            print(f"{name} is already in the phonebook.")
        
        number = input("Number: ")

        # Check if the number already exists for any name
        if number in phonebook.values():
            print(f"{number} is already associated with another contact.")
        
        # If name already exists, we append the number to the list of numbers
        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number]  # Add new name with a list of numbers

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name, numbers in phonebook.items():
        print(f"{name} -> {', '.join(numbers)}")


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # Break when user enters a blank line
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook")
        else:
            # If multiple numbers are associated with the name, show them
            print(f"Phone numbers for {name}: {', '.join(phonebook[name])}")


def main():
    phonebook = read_phone_numbers()  # Get the phonebook from user input
    print("\nPhonebook Entries:")
    print_phonebook(phonebook)  # Print all phonebook entries
    print("\nPhonebook Lookup:")
    lookup_numbers(phonebook)  # Allow the user to look up numbers


# Python boilerplate.
if __name__ == '__main__':
    main()

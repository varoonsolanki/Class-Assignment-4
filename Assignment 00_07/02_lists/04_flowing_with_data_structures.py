def add_three_copies(my_list, data):
    # Adds 3 copies of 'data' to the list 'my_list'
    for i in range(3):
        my_list.append(data)

# Main function to execute the code
def main():
    # Ask the user for a message to copy
    message = input("Enter a message to copy: ")
    
    # Initialize an empty list to store the copies
    my_list = []
    
    # Print the list before calling the function (should be empty initially)
    print("List before:", my_list)
    
    # Call the function to add 3 copies of the message to the list
    add_three_copies(my_list, message)
    
    # Print the list after the function call
    print("List after:", my_list)

# This line ensures the main function runs when the script is executed
if __name__ == "__main__":
    main()

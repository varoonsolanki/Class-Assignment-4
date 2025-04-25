def list_practice():
    # Create a list of fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' to the end
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Modified list: {lst}"
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if 0 <= start <= len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "One or both indices are out of range."

def index_game():
    sample_list = ['red', 'green', 'blue', 'yellow', 'purple']

    while True:
        print("\n--- List Game Menu ---")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            index = int(input("Enter index to access: "))
            print("Result:", access_element(sample_list, index))
        
        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(sample_list, index, new_value))
        
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(sample_list, start, end))

        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

        print("Current list:", sample_list)

def main():
    print(">>> Problem 1 Output:")
    list_practice()
    
    print("\n>>> Starting Problem 2 (Index Game):")
    index_game()

if __name__ == '__main__':
    main()

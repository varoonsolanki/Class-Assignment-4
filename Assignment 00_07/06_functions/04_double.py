def double(num: int):
    return num * 2

def main():
    num = int(input("Enter a number: "))  # Ask user for input and convert it to integer
    num_times_2 = double(num)  # Call the double function to multiply the number by 2
    print("Double that is", num_times_2)  # Print the result

if __name__ == '__main__':
    main()  # Call the main function when the script is run

def main():
    for i in range(10, 20):  # Loop through the numbers from 10 to 19
        if is_odd(i):  # Check if the number is odd
            print(f"{i} odd")  # Print the number and 'odd'
        else:
            print(f"{i} even")  # Print the number and 'even'

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Loop starts from 1 and goes up to num (inclusive)
        if num % i == 0:  # If num is divisible by i (no remainder)
            print(i)  # Print the divisor

def main():
    num = int(input("Enter a number: "))  # Ask the user to input a number
    print_divisors(num)  # Call the print_divisors function

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

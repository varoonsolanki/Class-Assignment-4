def print_ones_digit(num):
    # The ones digit of a number can be obtained by taking the remainder when divided by 10
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()

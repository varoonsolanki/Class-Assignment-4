import random

N_NUMBERS : int = 10  # Number of random numbers to generate
MIN_VALUE : int = 1    # Minimum value (inclusive)
MAX_VALUE : int = 100  # Maximum value (inclusive)

def main():
    for _ in range(N_NUMBERS):  # Repeat N_NUMBERS times
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Generate and print a random number on the same line

if __name__ == '__main__':
    main()

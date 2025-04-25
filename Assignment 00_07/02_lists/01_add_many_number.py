def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far

def main():
    print("Welcome to the Sum Calculator Form!")
    input_string = input("Enter numbers separated by commas (e.g. 1,2,3,4): ")
    
    # Split the input string into a list and convert each item to an integer
    try:
        numbers = [int(num.strip()) for num in input_string.split(",")]
        sum_of_numbers = add_many_numbers(numbers)
        print(f"The sum of your numbers is: {sum_of_numbers}")
    except ValueError:
        print("Please enter only valid numbers separated by commas.")

if __name__ == '__main__':
    main()

def main():
    print("Welcome to the Number Doubler Form!")
    input_string = input("Enter numbers separated by commas (e.g. 1,2,3,4): ")

    try:
        numbers: list[int] = [int(num.strip()) for num in input_string.split(",")]

        for i in range(len(numbers)):
            numbers[i] = numbers[i] * 2

        print(f"Doubled numbers: {numbers}")
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")

if __name__ == '__main__':
    main()

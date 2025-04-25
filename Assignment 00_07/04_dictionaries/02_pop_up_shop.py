def main():
    # Dictionary of fruits with prices
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0.0

    print("Welcome to the Fruit Cost Calculator!\n")
    
    for fruit, price in fruits.items():
        while True:
            try:
                qty = input(f"How many ({fruit}) do you want to buy?: ")
                if qty == "":
                    qty = 0  # Treat blank input as 0
                qty = int(qty)
                if qty < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += price * qty
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Display total with 2 decimal places
    print(f"\nYour total is ${total_cost:.2f}")


# Call the main function
if __name__ == '__main__':
    main()

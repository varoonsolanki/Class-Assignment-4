import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    guess_count = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            if guess < secret_number:
                print("Your guess is too low.\n")
            elif guess > secret_number:
                print("Your guess is too high.\n")
            else:
                print(f"🎉 Congrats! The number was {secret_number}.")
                print(f"You guessed it in {guess_count} tries.")
                break
        except ValueError:
            print("❌ Please enter a valid number.\n")

if __name__ == '__main__':
    main()

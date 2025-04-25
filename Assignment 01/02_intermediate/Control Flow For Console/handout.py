import random

NUM_ROUNDS = 5  # Number of rounds the player will play

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0  # Start with a score of 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        # Generate the random numbers for the player and the computer
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        
        # Display the player's number
        print(f"Your number is {your_number}")
        
        # Get the user's guess about whether their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Check if the guess is valid
        while guess not in ['higher', 'lower']:
            print("Please enter either 'higher' or 'lower'.")
            guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Determine if the guess was correct
        if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Print the current score after each round
        print(f"Your score is now {score}")
        print()  # Blank line to separate rounds

    # End of the game, print final message based on score
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()

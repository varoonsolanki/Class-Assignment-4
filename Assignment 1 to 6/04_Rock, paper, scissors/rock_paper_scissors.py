import random

print("🎮 Rock, Paper, Scissors Game")
print("Choose: rock, paper, or scissors\n")

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
rounds = 3

for i in range(rounds):
    print(f"\n🔁 Round {i + 1} of {rounds}")
    user = input("Your choice: ").lower()
    computer = random.choice(choices)
    print(f"🤖 Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("✅ You win this round!")
        user_score += 1
    elif user in choices:
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("⚠️ Invalid input! No points this round.")

# Final results
print("\n🏁 Game Over!")
print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")

if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif user_score < computer_score:
    print("💻 Computer wins the game! Better luck next time.")
else:
    print("🤝 It's a draw!")

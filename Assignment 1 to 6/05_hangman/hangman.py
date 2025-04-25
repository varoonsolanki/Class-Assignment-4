
import random

# Word list
words = ['python', 'hangman', 'program', 'developer', 'laptop', 'game', 'keyboard', 'monitor']

# Choose a random word
word = random.choice(words)
guessed_letters = []
tries = 6  # Number of wrong attempts allowed

print("🎮 Welcome to Hangman!")
print(f"The word has {len(word)} letters.\n")

# Display blanks
display_word = ["_" for _ in word]

# Game loop
while tries > 0 and "_" in display_word:
    print("Word: " + " ".join(display_word))
    print(f"🔁 Tries left: {tries}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⛔ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!\n")
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        tries -= 1

# Game result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)


import random

print("🎯 Welcome to the Guess the Number Game!")
print("Main ne 1 se 100 tak ek number socha hai.")
print("Tum usay guess karo! 🔍")

# Computer random number sochta hai
secret_number = random.randint(1, 100)
guess = None
attempts = 0

# Jab tak guess sahi nahi hota
while guess != secret_number:
    try:
        guess = int(input("Apna guess likho (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("📉 Bohat chhota hai! Try again.")
        elif guess > secret_number:
            print("📈 Bohat bara hai! Try again.")
        else:
            print(f"🎉 Mubarak ho! Tumne sahi guess kiya in {attempts} attempts! ✅")
    except ValueError:
        print("⚠️ Sirf number likho (1-100)!")


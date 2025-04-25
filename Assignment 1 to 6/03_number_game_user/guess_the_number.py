
def computer_guess():
    low = 1
    high = 100
    attempts = 0

    print("🧠 Tumne 1 se 100 tak ek number soch liya?")
    print("Main guess karunga. Tum sirf batao:")
    print("- 'h' agar mera guess bara hai")
    print("- 'l' agar mera guess chhota hai")
    print("- 'c' agar sahi guess hai ✅\n")

    while True:
        if low > high:
            print("😵 Tumne kuch galat input diya. Game over!")
            break

        guess = (low + high) // 2
        attempts += 1
        print(f"📢 Mera guess hai: {guess}")
        feedback = input("Tumhara response (h/l/c): ").lower()

        if feedback == 'c':
            print(f"🎉 Yay! Maine sahi guess kiya in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("⚠️ Sirf 'h', 'l', ya 'c' likho.")

# Game run
computer_guess()

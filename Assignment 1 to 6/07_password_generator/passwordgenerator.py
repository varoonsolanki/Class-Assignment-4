import random
import string

def generate_password(length):
    if length < 4:
        return "⚠️ Length kam se kam 4 honi chahiye!"

    # All characters pool
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill remaining length randomly
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# User input
try:
    length = int(input("🔐 Password ki length batao: "))
    password = generate_password(length)
    print(f"\n🧾 Tumhara strong password: {password}")
except ValueError:
    print("⚠️ Sirf numbers likho password length ke liye.")
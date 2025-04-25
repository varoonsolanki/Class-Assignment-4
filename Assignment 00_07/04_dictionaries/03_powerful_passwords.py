from hashlib import sha256

def hash_password(password):
    """
    Takes a password and returns its SHA256 hash.
    """
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    """
    Checks if the email exists and verifies the hashed password.
    Returns True if match found, otherwise False.
    """
    if email not in stored_logins:
        print("Email not found!")
        return False

    hashed_input = hash_password(password_to_check)
    stored_hash = stored_logins[email]

    return hashed_input == stored_hash

def main():
    # Stored logins with SHA256 hashed passwords
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # password
    }

    print(login("example@gmail.com", stored_logins, "word"))         # ❌ False
    print(login("example@gmail.com", stored_logins, "password"))     # ✅ True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))   # ✅ True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   # ❌ False

    print(login("student@stanford.edu", stored_logins, "password"))  # ✅ True
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # ❌ False
    print(login("not_found@email.com", stored_logins, "anything"))   # ❌ Email not found!

if __name__ == '__main__':
    main()

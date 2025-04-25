ADULT_AGE = 18  # U.S. age for adulthood

def is_adult(age: int):
    # Check if age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == '__main__':
    main()

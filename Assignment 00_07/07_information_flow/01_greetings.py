def greet(name):
    return "Greetings " + name + "!"

def main():
    name = input("What's your name? ")
    print(greet(name))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

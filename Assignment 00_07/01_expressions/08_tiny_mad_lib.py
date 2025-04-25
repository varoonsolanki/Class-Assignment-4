SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "  # adjective noun verb

def main():
    # Prompt user for words
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Combine the inputs into the final sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

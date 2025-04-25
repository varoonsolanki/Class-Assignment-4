MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci number
    next_term = 1  # The 1st Fibonacci number

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Print all terms on the same line
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()

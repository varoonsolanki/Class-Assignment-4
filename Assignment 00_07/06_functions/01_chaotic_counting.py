import random

# Set the likelihood of stopping early (can be adjusted)
DONE_LIKELIHOOD = 0.3  # 30% chance of stopping

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():  # Check if we should stop early
            return  # Exit the function if done() returns True
        print(curr_num)  # Print the current number

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD  # If random number < DONE_LIKELIHOOD, return True

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Call the chaotic_counting function
    print("I'm done")  # Print this once chaotic_counting finishes

if __name__ == "__main__":
    main()

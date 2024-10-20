
def guess_number():
    print("Think of a number between 1 and 128.")

    # Setting the initial limits
    lower_limit = 1  # Lower limit
    upper_limit = 128  # Upper limit
    attempts = 0  # Attempt counter

    while attempts < 6:
        # Calculate the average value (M) between 'lower_limit' and 'upper_limit'
        M = (lower_limit + upper_limit) // 2
        attempts += 1

        # Ask if the number is M
        print(f"Attempt {attempts}: Is the number you're thinking of {M}?")
        response = input("Respond with (y)es, (n)o, or if it's (h)igher or (l)ower: ").strip().lower()

        if response == 'y':
            print(f"The number you're thinking of is {M}, and I guessed it in {attempts} attempts!")
            return
        elif response == 'h':
            # If the number is higher than M, reset the lower limit to M
            lower_limit = M + 1
        elif response == 'l':
            # If the number is lower than M, reset the upper limit to M
            upper_limit = M - 1
        else:
            print("Invalid response. Please answer with 'y', 'h', or 'l'.")

    # If the number of attempts is 6 and the number isn't found
    print("Sorry, I couldn't guess the number in 6 attempts.")


# Call the function to run the game
guess_number()


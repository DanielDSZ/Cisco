
## Number Guessing Game - Code Explanation

This Python code implements a **number guessing game** where the computer tries to guess a number that the user is thinking of, between 1 and 128. The program uses a **binary search strategy** to narrow down the possible numbers, aiming to guess the correct number within 6 attempts.

1. **Initial Setup**: 
   The computer prompts the user to think of a number between 1 and 128. It sets an initial lower limit (`lower_limit = 1`) and upper limit (`upper_limit = 128`), with a counter (`attempts`) to track the number of tries.

2. **Binary Search Algorithm**:
   In each iteration of the loop, the program calculates the middle point (`M`) between the current limits. It then asks the user if their number is equal to, higher, or lower than `M`. Depending on the user’s response:
   - If the number is higher, the lower limit is adjusted to `M + 1`.
   - If the number is lower, the upper limit is adjusted to `M - 1`.
   - If the number is correct, the game ends, and the number of attempts is displayed.

3. **User Input**:
   The program expects the user to input "yes" (`y`), "higher" (`h`), or "lower" (`l`) to guide the guessing process. If an invalid input is given, the program prompts the user to try again.

4. **Game End**:
   The game either concludes successfully when the number is guessed correctly, or it ends after 6 failed attempts, displaying a message saying the number couldn't be guessed.

This efficient approach ensures that the correct number is found in the least number of steps, utilizing the properties of binary search.

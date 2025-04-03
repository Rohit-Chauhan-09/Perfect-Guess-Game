# The Perfect Guess (Project)

''' We are going to write user program that generates user random number and asks the user to
guess it.
If the player's guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user's guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module. '''

import random
computerGuess = random.randint(1,100)

user = -1
guess = 0
while (user != computerGuess):
    user = int(input("Enter the Guess Number: "))

    if (user > computerGuess):
        print("Guess the Lower number please!")
        guess += 1

    elif (user < computerGuess):
        print("Guess the Higher number please!")
        guess += 1

print(f"Wow ! You guess the correct number {computerGuess} in {guess} attempts.")
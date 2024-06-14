"""
The random module is used to generate a random number and store it as secret number.
The while loop allows the user to make multiple guesses until they guess the correct secret number or choose to exit.
The if, elif, and else statements are used to check whether the guess is correct and provide feedback to the user.
The break statement is used to exit the loop when the correct guess is made or when the user chooses not to play again.
The program also uses input to get user input and int to convert the input to an integer.
"""

import random as ran
import string

ran_integer = ran.randint(1, 10)
ran.shuffle(ran_integer)

def guess():
    while True:
        print("There is a secret number that you have to guess")
        print("It's a number between 1 and 10")
        print("Please type the secret number below to exit the code")
        x = int(input(": "))
        if x == ran_integer:
            print("Congratulations!!!. You have guessed the correct number")
            print("You have exited the code!")
            break
        elif x != ran_integer:
            print("Im sorry you didn't guess the correct number")
            print("You have to try again")
            print("\n")
            guess()
        else:
            break


guess()

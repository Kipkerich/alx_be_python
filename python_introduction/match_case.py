import random

secret_number = int(random.randint(1, 100))

guess = int(input("Guess a number between 1 and 100: "))

match guess:
    case _ if guess == secret_number:
        print("Congratulations, You guessed it!")
    case _ if abs(guess - secret_number) <= 5:
        print("Very close! Try again.")
    case _ if abs(guess - secret_number) <= 10:
        print("Getting warmer. Try again.")
    case _ if guess < secret_number:
        print("Too low. Try again.")
    case _:
        print("Too high. Try again.")
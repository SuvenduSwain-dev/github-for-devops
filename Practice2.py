import random

# Generate a secret number between 1 and 10
secret_number = random.randint(1, 10)
guess = 0

print("I am thinking of a number between 1 and 10.")

# Keep asking the user until they guess correctly
while guess != secret_number:
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
         print("Correct! You win!");
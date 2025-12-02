"""
Ex: guessing_game 

description:

secret = 7

guess = input("Guess a Number: ")

if guess <...
    print('Too Low')
elif guess >...
    print('Too High)

"""

secret = 20
user_guess = int(input("Guess an integer: "))

while user_guess != secret:
    if user_guess < secret:
        print("Too low! Guess a larger number!")
    else:  # user_guess > secret
        print("Too high! Guess a smaller number!")
    user_guess = int(input("Guess an integer: "))
    
print("Good job! You guessed it!")
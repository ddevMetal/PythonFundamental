"""
Ex: guessing_game v.2

template answer from youtube solution

description:

secret = 7

guess = input("Guess a Number: ")

if guess <...
    print('Too Low')
elif guess >...
    print('Too High)

"""


# 🤔 Guess a number !
import random

# Rules
minVal      = 1
maxVal      = 60
secret_num  = random.randint(minVal, maxVal) # 😯 Set random number



for i in range(5):
    print('-'*50, f'attempt {i+1}/5')
    
    # Ask user for Input!
    guess = input(f'❓Guess the secret number between {minVal} and {maxVal}: ')
    guess = int(guess)

    #💡 Check for Input
    if guess < minVal or guess > maxVal:
        print (f'⛔Incorrect Input. Guess a number between {minVal} and {maxVal}')

    elif guess == secret_num:
        print("🎉Correct! You guessed it!")
        break

    elif guess > secret_num:
        print('❌ Too high! Try Again.')

    else:
        print('❌ Too low! Try Again.')




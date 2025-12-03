"""
Ex: guessing_game 

Improved guessing game with:
- Random number range
- Limited attempts
- Attempt counter
- Better feedback
"""
import random

# Generate random range for variety
min_val = random.randint(1, 20)
max_val = random.randint(50, 100)
secret = random.randint(min_val, max_val)

# Game settings
max_attempts = 5
attempts = 0

# Display game info
print(f"🎮 Guess the number between {min_val} and {max_val}!")
print(f"You have {max_attempts} attempts.\n")

# First guess
user_guess = int(input("Enter your guess: "))
attempts += 1

# Game loop
while user_guess != secret and attempts < max_attempts:
    if user_guess < secret:
        print(f"❌ Too low! Try higher.")
    else:
        print(f"❌ Too high! Try lower.")
    
    print(f"Attempts remaining: {max_attempts - attempts}")
    print("-" * 40)
    
    user_guess = int(input("Enter your guess: "))
    attempts += 1

# Check result
if user_guess == secret:
    print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s)!")
else:
    print(f"\n💀 Game Over! The number was {secret}.")
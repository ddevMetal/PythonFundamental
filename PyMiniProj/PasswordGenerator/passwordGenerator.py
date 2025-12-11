"""
Password Generator Explanation (Compressed Version)

url: https://www.youtube.com/watch?v=XCIBOl3FTKo

We start by preparing 3 separate character groups:
    letters  -> a-z and A-Z
    digits   -> 0-9
    special  -> punctuation symbols (!@#$%^&* etc.)

These come directly from the Python `string` module, which contains
predefined sets of characters for convenience.

We then build a final character pool:
    characters = letters
        (letters are always included)
    if numbers=True:
        characters += digits
    if special_characters=True:
        characters += special

This is like:
    d = a
    d' = d + b
    d'' = d' + c
So finally `characters` holds all allowed characters in one long string.

Next we generate a password one character at a time. Each new character
is randomly selected from the full `characters` pool.

Flags (`has_number`, `has_special`) keep track of whether the password
already contains a digit or special character. Once True, they stay True.

The loop continues until:
    1) all required criteria are satisfied (flags True)
    AND
    2) the password length reaches `min_length`.

Once both conditions are met, the loop ends and the final password is returned.
"""

# ============================================================================
# PASSWORD GENERATOR
# ============================================================================
# Generates secure random passwords with customizable requirements

import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    """
    Generate a random password meeting specified criteria.
    
    Parameters:
        min_length (int): Minimum password length
        numbers (bool): Include digits (0-9)
        special_characters (bool): Include special characters (!@#$%^&* etc.)
    
    Returns:
        str: Generated password meeting all requirements
    """
    
    # ---- Character Sets ----
    letters = string.ascii_letters      # Always includes a-z + A-Z
    digits = string.digits              # 0-9
    special = string.punctuation        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    
    # ---- Build the final character pool (letters always included) ----
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    # ---- Password + Tracking Flags ----
    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False
    
    # ---- Generate password until it meets all rules ----
    while not meet_criteria or len(pwd) < min_length:
        
        # Pick a random character from the full pool
        new_char = random.choice(characters)
        pwd += new_char
        
        # Update flags based on the type of character added
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # Check requirements (assume True, then verify)
        meet_criteria = True
        if numbers:
            meet_criteria &= has_number
        if special_characters:
            meet_criteria &= has_special
    
    return pwd


# ============================================================================
# USER INPUT & PASSWORD GENERATION
# ============================================================================

min_length = int(input("Enter minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd1 = generate_password(min_length, has_number, has_special)

print(f'The generated password is: {pwd1}')

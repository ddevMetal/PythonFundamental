# Is Your Password Secure 🔐?


# User Input (username and password)
print(f"{'-'*50}\n📃 Creating a New Account.\n{'-'*50} " )
username = input("Username: ")
password = input("Password: ")
print(f'{'-'*50}')

def check_password(password):
    """
    Password Checker

    Input requirement: 
    - 8+ Char
    - has lowercase
    - has uppercase
    - has a digit
    - has a symbol
    """

    # 📦 Place Holders
    symbol = '!@#$%^&*()_+-=[]{}|;:\'"\\,.<>?/`~'  # ✅ Simple string, not regex
    check_length = False
    check_digit = False
    check_lower = False
    check_upper = False
    check_symbol = False
    check_nospaces = False

    # Security Checks
    # ✅ Length (minimum 8 characters)
    if len(password) >= 8:
        check_length = True


    # ✅ Contains at least one digit

    for char in password:
        if char.isdigit():
            check_digit = True

        # ✅ Contains at least one uppercase letter
        elif char.isupper():
            check_upper = True
        # ✅ Contains at least one lowercase letter
        elif char.islower():
            check_lower = True
        # ✅ Contains at least one one special character   
        elif char in symbol:
            check_symbol = True

    # ✅ Check for no spaces
    if ' ' not in password:  # ✅ Check password, not boolean
        check_nospaces = True

    # Display Results

    checks = [ check_length,
                check_digit,
                check_lower,
                check_upper,
                check_symbol,
                check_nospaces ]

    if all(checks):
        print("✅ Account Created Successfully.")
    else:
        print('❌ Password is not strong enough.\n')

        if not check_length:
            print('   • Password must be at least 8 characters long')
    
        if not check_digit:
            print('   • Password must contain at least 1 digit (0-9)')

        if not check_upper:
            print('   • Password must contain at least 1 uppercase letter (A-Z)')

        if not check_lower:
            print('   • Password must contain at least 1 lowercase letter (a-z)')

        if not check_symbol:
            print('   • Password must contain at least 1 symbol (!@#$%^&* etc.)')

        if not check_nospaces:
            print('   • Password must not contain spaces')


# Call the function
check_password(password)


# Call the function to check the password
check_password(password)

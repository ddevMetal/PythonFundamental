"""
Password Checker

Input requirement: 
- 8+ Char
- has lowercase
- has uppercase
- has a digit
- has a symbol
"""


def pwValidator(pw):
    """
    Validates password against all requirements.
    Returns: tuple (is_valid, has_upper, has_lower, has_digit, has_symbol)
    """
    has_upper = any(c.isupper() for c in pw)  # Check for uppercase letters (A-Z)
    has_lower = any(c.islower() for c in pw)  # Check for lowercase letters (a-z)
    has_digit = any(c.isdigit() for c in pw)  # Check for digits (0-9)
    # Check for symbols - exclude alphanumeric and spaces
    has_symbol = any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for c in pw)

    is_valid = has_upper and has_lower and has_digit and has_symbol
    return is_valid, has_upper, has_lower, has_digit, has_symbol


def userEnterPassword():
    """
    Prompts user for password and validates it.
    Loops until a valid password is entered.
    Returns: validated password string
    """
    while True:
        password = input("Please enter password: ")

        # Check for empty or whitespace-only input
        if not password.strip():
            print("❌ Password cannot be blank!\n")
            continue

        # Check minimum length requirement
        if len(password) < 8:
            print(f"❌ Password must have at least 8 characters! (You entered {len(password)})\n")
            continue

        # Validate all password requirements
        is_valid, has_upper, has_lower, has_digit, has_symbol = pwValidator(password)
        
        if not is_valid:
            print("\n❌ Password does not meet requirements:")
            # Show specific missing requirements
            if not has_upper:
                print("   • Missing at least 1 uppercase letter (A-Z)")
            if not has_lower:
                print("   • Missing at least 1 lowercase letter (a-z)")
            if not has_digit:
                print("   • Missing at least 1 digit (0-9)")
            if not has_symbol:
                print("   • Missing at least 1 symbol (!@#$%^&* etc.)")
            print()  # Empty line for readability
            continue
        
        # All checks passed - return valid password
        return password



# Main execution
#---------------------------------------------------------
print("=" * 50)
print("🔒 PASSWORD STRENGTH CHECKER 🔒")
print("=" * 50)
print("\nPassword Requirements:")
print("✓ At least 8 characters")
print("✓ At least 1 uppercase letter")
print("✓ At least 1 lowercase letter")
print("✓ At least 1 digit")
print("✓ At least 1 symbol (!@#$%^&* etc.)")
print()

# Get validated password
p1 = userEnterPassword()

# Success message
print("\n" + "=" * 50)
print("✅ PASSWORD ACCEPTED!")
print("=" * 50)
print(f"Your password: {p1}")
print(f"Password length: {len(p1)} characters")
print("\n💪 Strong password created successfully!")


"""
Sum of Digits

This task in this mission is as follows:
    - you are given an integer. If it consists of one digit, simply return its value.
    = if it consists of two of more digit, add them until the nuber contains only one digt and return it

    Examples: 
    38 -> 3 + 8 = 11, 11 -> 1 + 1 = 2    (2 is the answer)

    9999 -> 9 + 9 + 9 + 9 = 36
            36 -> 3 + 6 = 9              (9 is the answer)
"""



def sumOfDigit(n):
    print(f"→ enter({n})")

    if n < 10:
        print(f"← return {n}")
        return n

    total = sum(int(i) for i in str(n))
    result = sumOfDigit(total)

    print(f"← return {result} from {n}")
    return result




def sumOfDigit2(number):

    # 🅰 Base Case (Return Single Digit)
    if number < 10:
        return number 
    
    # 🅱 Recursive case (calculate Digits Sum)
    digits = []
    for str_num in str(number):
        num = int(str_num)
        digits.append(num)

    total = sum(digits)

    return sumOfDigit2(total) # Recursive call






# # sumOfDigit(9)
# sumOfDigit(21231230)


# Testing with assert
print("="*60)
print("🧪 Testing sumOfDigit2 with assertions")
print("="*60)

# Test 1: Example from docstring
assert sumOfDigit2(38) == 2, "38 → 3+8=11 → 1+1=2"
print("✅ Test 1 passed: sumOfDigit2(38) == 2")

# Test 2: Edge case - zero
assert sumOfDigit2(0) == 0, "0 should return 0"
print("✅ Test 2 passed: sumOfDigit2(0) == 0")

# Test 3: Single digit
assert sumOfDigit2(9) == 9, "Single digit should return itself"
print("✅ Test 3 passed: sumOfDigit2(9) == 9")

# Test 4: Example from docstring
assert sumOfDigit2(9999) == 9, "9999 → 36 → 9"
print("✅ Test 4 passed: sumOfDigit2(9999) == 9")

# Test 5: Additional test
assert sumOfDigit2(123) == 6, "123 → 1+2+3=6"
print("✅ Test 5 passed: sumOfDigit2(123) == 6")

# Test 6: Large number
assert sumOfDigit2(21231230) == 5, "21231230 → 14 → 5"
print("✅ Test 6 passed: sumOfDigit2(21231230) == 5")

print("\n" + "="*60)
print("🎉 All tests passed!")
print("="*60)
assert sumOfDigit2(9999) == 9
assert sumOfDigit2(811) == 1
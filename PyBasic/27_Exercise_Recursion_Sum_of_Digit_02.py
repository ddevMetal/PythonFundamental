def sumOfDigitIter(n):
    print(f"🔢 Starting with: {n}")
    
    while n > 9:
        # Extract digits as a list (not generator)
        digit = [int(i) for i in str(n)]  # ✅ Use [] for list
        total = sum(digit)
        
        print(f"   Digits: {digit} → Sum: {total}")
        
        n = total  # ✅ Update n to continue the loop
    
    print(f"✅ Final result: {n}")
    return n



result = sumOfDigitIter(123123123)
print(f"\n🎯 Answer: {result}")
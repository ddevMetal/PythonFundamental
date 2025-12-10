# ❓ What is Factorial?

# Factorial is the product ofd all numbers form 1 to n.
# 3! = 3*2*1        = 6
# 4! = 4*3*2*1      = 24
# 5! = 5*4*3*2*1    = 120
#--------------------------------------------------



# 🅱 FACTORIAL - LOOP
#--------------------------------------------------
def factorial(n):
    result = 1
    while True:
        if n == 0:
            break
        result *= n
        n -= 1

    return result

print('Iterative')
print(factorial(5))
print('--------------------------------------------')

 

#  FACTORIAL - RECURSIVE
#--------------------------------------------------
def factorialRecur (n):
    print(f'Entering Factorial: {n}')
    # base case
    if n == 0:
        print(f'Base Case Reaches: Returning {n}')
        return 1
    
    result = n * factorialRecur(n-1) # Recursive Case
    print(f'Retuning {result} for factorial ({n})')
    return result 



print('Recursive')
print(factorialRecur(5))
print('--------------------------------------------')


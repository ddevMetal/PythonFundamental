def br(n):
    return  print('-'*n)

# Resursive Functions

# 🅰 Iterative Countdown
#--------------------------------------------------

def countdownIter(n):
    while True:
        if n < 0:
            break
        print(n)
        n -= 1

print('Iteratice')
countdownIter(5)
br(50)






# 🅱 Recursive Countdown
#--------------------------------------------------
def countdownRecur(n):
    # Base case
    if n < 0:
        return n
    
    # Recursive Case
    print(n)
    countdownRecur(n - 1)

print('Recursive')
countdownRecur(5)
br(50)

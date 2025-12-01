from helper import br, ctitle

# Basic Operators in Python: Arithmetic

# # Expression : Sn Expression in Python is a combination of values, variables, operators, and
# #              function calls that can produce a result e.g. 2+2 is an expression.

# Arithmetic Operators
a = 10
b = 3

print("a: " + str(a))
print("b: " + str(b))
br(50)


# Arimetic operators
#-------------------------------------------------------------------------------------------------
print("a + b =", a + b)         # 10 +  3 = 13           (addition)
print("a - b =", a - b)         # 10 -  3 = 7            (subtraction)
print("a * b =", a * b)         # 10 *  3 = 30           (multiplication)
print("a / b =", a / b)         # 10 /  3 = 3.3333       (division)
print("a // b =", a // b)       # 10 // 3 = 3            (floor division)
print("a % b =", a % b)         # 10 %  3 = 1            (mudulo)
print("a ** b =", a ** b)       # 10 ** 3 = 1000         (numeric power) 10  ^ 3


# use case for modulo operator
"""
# Odd (%2 will be 1)

num = 10
is_even = num % 2 == 0
is_odd = numm % 2 == 1
print(is_even) #True
print(is_odd)  #False


this can be use to even and odd number filtering etc...
"""
print()
br(50)


# Comparison operators
#-------------------------------------------------------------------------------------------------
print("a > b    =  ", a > b )         # 10 >  3 = True          (Greater Than)
print("a < b    =  ", a < b )         # 10 <  3 = False         (Less Than)
print("a >= b   =  ", a >= b)         # 10 >= 3 = True          (Greater Than or Equals To)
print("a <= b   =  ", a <= b)         # 10 <= 3 = False         (Less Than or Equal To)
print("a == b   =  ", a == b)         # 10 == 3 = False         (Equality)
print("a != b   =  ", a != b)         # 10 != 3 = True          (Inequality)

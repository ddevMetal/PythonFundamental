# Basic Operators in Python

# # Expression : Sn Expression in Python is a combination of values, variables, operators, and
# #              function calls that can produce a result e.g. 2+2 is an expression.

# x = 10
# y = 20
# z = 10 + y + 10 + y + 10 + y

# y = z ** 3

# print(x,y,z)


# #-----------------------------------------------------------------------------------------------
# #🔠 String Operators

# # Join Strings
# a = "Hello"
# b = "World"
# c = a + b       # Joining String is called concat
# print(c)


name = 'Chee Bai'

# # Method 1:
# print ("My Name is " + name)

# # Method 2:
# print('My Name is: {}'.format('Ch'))


# # Multiply Strings
# print('Hello')
# print('-'*100)
# print('Hello\n'*100)        #\n new line


# # Membership Operators : ---> in or not in
# message  = "We need to build a brick wall"
# print('brick' in message ) #True
# print('Brick' in message) #False
# print('glass' in message)
# print ('glass' not in message)


# Equals/ Not Equals operator (==, !=)
a = 'Concrete-10cm'
b = 'Concrete-20cm'

check = a == b
print(a==b) # False
print(a!=b)
from helper import br, ctitle


# #1️⃣1️ function template
# # syntax basic
# def say_hello():
#     print('Hello BIM World!')



# #2️⃣ function with parameters/ arguement
# def greet(msg):
#     print(f"Msg: {msg}")

# # execute function
# say_hello()

# greet("Cheese Bai")
# greet("Lan Jiao")

# function with 2 parameters/ arugments
def greet(name, salutation=""):
    print('Hello {} {}!'.format(salutation, name))


greet("chee bong", "mr")


#3️⃣ return value
"""
a = 5
b = 10

total = a + b

print("{} + {} = {}".format(a,b,total))
"""

def add_number(a, b):
    total = a + b
    print ("{} + {} = {}".format(a,b,total))
    return total



# calling the function
x = add_number(5,12)
y = add_number(88,89)

print(x,y)


def say_hello():
    print ('Hellow BIM World!')

say_hello()
say_hello()
say_hello()


# 2️⃣ Function with Arguments/ Parameters
"""
Function Anatomy:

def function_name(x,y):
____# code inside


x,y --> parameter/arguements

"""
def greet(name=None):  # Default parameter value
    if name == None:
        print(f'Hello Dog!')
    else:
        print(f'Hello {name}!')
        


greet()  # Uses default None → prints "Hello Dog!"
greet("chee bai gou")  # Prints "Hello chee bai gou!"
greet("lam pa")

br(50)

def tio_taiji(total_pax, gang_name=''):
    print('Lanjiao gang -> {},total pax{}'.format(gang_name, total_pax))

tio_taiji(100, "Salakau")
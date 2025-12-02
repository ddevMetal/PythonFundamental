from helper import br, ctitle

# #1️⃣ Logic - Basic Syntax
# condition = 5>0

# if condition:
#     print ("5 Greater than 0")
#     print("Code A")
#     print("Code A")
#     print("Code A")
#     print("Code A")
# else:
#     print("5 Less than 0")


#2️⃣ Example 2 If/ Elif/ Else
# not a good example

temp = 1

if temp > 25:
    print("Its really hot outside 😖")
elif temp > 15:
    print("Its warm outside! 😊")
else:
    print("Its cold outside! 🥶")


br(50)

#3️⃣ 
# using logical operator
logical_and = True and True #True
logical_or = True or False  # True
logical_not = not True      # False

x = 20
y = 40

# method 1
if x > 0 and x < 100 and y > 0 and y < 100:
    print("XY coordinate is Good!")

# method 2 : same 
if x > 0:
    if x < 100:
        if y > 0:
            if y < 100:
                print("XY IS GOOD!")

br(50)
# logical not
is_enabled = False

if not is_enabled:
    print("All Bad!")




br(50)
# membership operator
member_in               = 'wood'    in ['metal', 'concrete', 'wood']
member_in               = 'wood'    in 'wood'
member_not_in           = 'wood'    in ['metal', 'concrete', 'bricks']



# nested statement
panel_w = 2000
panel_h = 2500

if panel_w <= 1500:
    print('width is good')
    if panel_h <= 3000:
        print('height is good')
    else:
        print('height is not good')
else:
    print('width is not good')
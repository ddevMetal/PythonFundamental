from helper import br, ctitle


# ## Basic for loop structure 

# container = [1,2,3,4,5]

# for i in container:
#     print(i)

#     if i == 2:
#         print('Number 2')
        


# #1 Loop over list
# #------------------------------------------------------------------------
# list_material = ["wood", "steel", "plastic", "glass", "rubber"]

# for mat in list_material:
#     print(mat)

# br(50)



# #2 Looop Over String
# #------------------------------------------------------------------------
# text = "Hello Python Hackers"

# for char in text:
#     lowerChar = char.lower()
#     upperChar = char.upper()
#     print(f"{lowerChar} --- {upperChar}")
# br(50)


# #3 Loop over Digits
# #------------------------------------------------------------------------ 
# big_number = 123456789

# for str_num in str(big_number):
#     num = int(str_num)
#     sq = num**2
#     cube = num**3
#     print(num, sq, cube)

# br(50)


# #4 Working with range in For Loop

# """
# range(a,b,c)

# a -> start: 1       // begin at 1
# b -> stop: 200      // Stop before 200(doesn't include 200)
# c -> step: 10       // increment by 10 each time

# """

# #EX: 1
# for i in range(1,200,10):
#     print(i)


# #EX: 2 - Dynamically adding items to a list using a loop
# # Start with 5 floor plans in the list
# floor_plans = ["entrance hall", "master suite", "guest room", "office", "garage"]

# # Loop 10 times (i goes from 1 to 10)
# for i in range(1, 11):  # range(1, 11) produces: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    
#     # Create a name for each floor plan using f-string
#     plan_name = f'FloorPlan_{i}'  # Results: FloorPlan_1, FloorPlan_2, ..., FloorPlan_10
    
#     # Add the new plan name to the end of the list
#     floor_plans.append(plan_name)  # append() adds item to end of list

# # Print the final list (now has 15 items: 5 original + 10 generated)
# print(floor_plans) 

# br(50)


# #5 Break out of For-Loops
# #---------------------------------------------------
# nums = [99, 1, 23, 33, 40 , 57, 6, 81, 2, 10,24,19]

# for n in nums:
#     if n%2 == 0 and n != 0:
#         print(f"First Even Number: {n}")
#         break

# print('Finished.')



# #6 Continue Iteration
# #---------------------------------------------------
# """
# concept:
# real_money = (5, 10, 20, 50, 100, 200, 500) #EUR
# wallet = [5, 20, 10, 25, 10 ,50]
#                       ^    25 != real_money continue total = (5+20+10+10+50) = 95
# """
# real_money = (5, 10, 20, 50, 100, 200, 500) #EUR
# wallet = [5, 20, 10, 25, 10 ,50]

# total = 0

# for note in wallet:
#     if note not in real_money:
#         continue
    
#     total += note
# print(f'Total: {total} EUR')
# br(50)




# #7 Nested Loop
# #---------------------------------------------------
# course = [
#     ['Lesson_01.01','Lesson_01.02','Lesson_01.03','Lesson_01.04'],
#     ['Lesson_02.01','Lesson_02.02','Lesson_02.03'],
#     ['Lesson_03.01','Lesson_03.02']
# ]

# for module in course:
#     print(f"Starting Module: {module}\n")

#     for lesson in module:
#         print(f"Completed: {lesson}")
    
#     print("Module is Completed!")
#     br(6)



# #EX:2
# qty = 5

# for x in range(qty):
#     for y in range(qty):
#         print('*'*y)
# print('---')


#8 While Loop
"""
count = 0

while count < 100:
    print(count)
    count += 1

"""
#---------------------------------------------------

#Iterable Object
list_nums   = [1,2,3,4,5,6,7,8,9,10]
list_items  = ['a', 'b', 'c', 'd']
tuple_nums  = (1,2,3,4,5)
string      = 'Text is a sequence of characters!'
range_10    = range(100)
dict_itmes  = {'key1': 'value1', 'key2':'value2'}


#9 Ticketing Machine Example
#---------------------------------------------------

tickets = 100

while True:
    n = input('Buy Ticket: ')
    n = int(n)

    if tickets - n <0:
        print('⚠Not enough tickets. Try again.')
        continue
    # Sell Tickets
    tickets -= n
    print(f'Tickets Left: {tickets}')

    if tickets == 0:
        print('Sold out!')
        break
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


#8 While Loop with Conditionals
"""
Basic while loop setup:

count = 0
while count < 100:
    print(count)
    count += 1
"""
#---------------------------------------------------

# Iterable Objects Reference
list_nums   = [1,2,3,4,5,6,7,8,9,10]
list_items  = ['a', 'b', 'c', 'd']
tuple_nums  = (1,2,3,4,5)
string      = 'Text is a sequence of characters!'
range_10    = range(100)
dict_items  = {'key1': 'value1', 'key2':'value2'}



#EX 1: While Loop with Break
#---------------------------------------------------
"""
Explanation: Loop runs indefinitely (while True) until a condition triggers 'break'
Use case: When you don't know how many iterations needed
"""
tickets = 100

while True:
    n = input('Buy Ticket: ')
    n = int(n)

    if tickets - n < 0:
        print('⚠Not enough tickets. Try again.')
        continue  # Skip rest of loop, start next iteration
    
    # Sell Tickets
    tickets -= n
    print(f'Tickets Left: {tickets}')

    if tickets == 0:
        print('Sold out!')
        break  # Exit loop completely



#EX 2: While Loop with Counter (Standard Pattern)
#---------------------------------------------------
"""
Explanation: Loop runs while condition is True, with counter increment
Use case: When you know the stopping condition
"""
count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1
print("Loop finished!")



#EX 3: Sentinel-Controlled Loop (User Input Termination)
#---------------------------------------------------
"""
Explanation: Loop continues until user enters a specific 'sentinel' value
Use case: Processing user input until they want to quit
"""
total = 0

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    if user_input.lower() == 'q':  # Sentinel value
        break
    
    total += int(user_input)
    print(f"Running total: {total}")

print(f"Final total: {total}")



#EX 4: Condition-Controlled Loop (Event-Based)
#---------------------------------------------------
"""
Explanation: Loop continues until a specific condition is met
Use case: Waiting for a specific state/value
"""
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_pass = input("Enter password: ")
    
    if user_pass == password:
        print("✅ Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Wrong! {remaining} attempts left.")
        else:
            print("🔒 Account locked!")



#EX 5: While Loop with Continue (Skip Iteration)
#---------------------------------------------------
"""
Explanation: 'continue' skips rest of current iteration and goes to next
Use case: Filtering out unwanted values while processing
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers):
    num = numbers[i]
    i += 1
    
    if num % 2 != 0:  # If odd number
        continue      # Skip to next iteration
    
    print(f"Even number: {num}")



#EX 6: Nested While Loops
#---------------------------------------------------
"""
Explanation: While loop inside another while loop
Use case: Multi-level iteration (like matrix traversal)
"""
rows = 3
cols = 3
i = 0

while i < rows:
    j = 0
    while j < cols:
        print(f"({i},{j})", end=" ")
        j += 1
    print()  # New line after each row
    i += 1



#EX 7: While-Else Pattern
#---------------------------------------------------
"""
Explanation: 'else' block executes when loop completes normally (not via break)
Use case: Determining if loop completed or was interrupted
"""
search_value = 50
numbers = [10, 20, 30, 40, 60]
i = 0

while i < len(numbers):
    if numbers[i] == search_value:
        print(f"Found {search_value} at index {i}!")
        break
    i += 1
else:
    print(f"{search_value} not found in list.")



#EX 8: Flag-Controlled Loop
#---------------------------------------------------
"""
Explanation: Boolean flag variable controls loop execution
Use case: When multiple conditions can end the loop
"""
is_running = True
health = 100

while is_running:
    action = input("Choose action (attack/heal/quit): ").lower()
    
    if action == 'attack':
        health -= 20
        print(f"Took damage! Health: {health}")
        
        if health <= 0:
            print("💀 Game Over!")
            is_running = False  # Change flag to end loop
    
    elif action == 'heal':
        health = min(100, health + 30)  # Max 100
        print(f"Healed! Health: {health}")
    
    elif action == 'quit':
        print("Thanks for playing!")
        is_running = False  # Change flag to end loop
    
    else:
        print("Invalid action!")



#EX 9: Menu-Driven Loop
#---------------------------------------------------
"""
Explanation: Displays menu, processes choice, repeats until exit
Use case: Interactive programs with multiple options
"""
while True:
    print("\n=== MENU ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    
    choice = input("Select option: ")
    
    if choice == '1':
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Result: {a + b}")
    
    elif choice == '2':
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print(f"Result: {a - b}")
    
    elif choice == '3':
        print("Goodbye!")
        break
    
    else:
        print("Invalid option!")



#EX 10: Do-While Pattern (Python Style)
#---------------------------------------------------
"""
Explanation: Ensures loop runs at least once (Python doesn't have do-while)
Use case: When you need to execute loop body before checking condition
"""
# Python doesn't have do-while, so we simulate it
while True:
    # Loop body executes first
    number = int(input("Enter positive number: "))
    print(f"You entered: {number}")
    
    # Condition checked at end
    if number > 0:
        break
    else:
        print("Must be positive! Try again.")

print("Valid number entered!")



#==========================================================================
# SECTION 9: Mixed Loop & Conditional Patterns
#==========================================================================
"""
Different ways to combine loops (for/while) with conditionals (if/elif/else)
"""


#EX 1: For Loop + If/Else (Filtering)
#---------------------------------------------------
"""
Explanation: Use if/else inside for loop to filter and categorize items
Use case: Processing list items with different actions
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is EVEN")
    else:
        print(f"{num} is ODD")



#EX 2: For Loop + If/Elif/Else (Multi-Category)
#---------------------------------------------------
"""
Explanation: Multiple conditions to categorize items in different ways
Use case: Grading system, status checking, tier classification
"""
scores = [95, 78, 85, 62, 45, 88, 91]

for score in scores:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    print(f"Score: {score} → Grade: {grade}")



#EX 3: Nested For Loops + If (2D Array Processing)
#---------------------------------------------------
"""
Explanation: Nested loops with conditional to find specific values
Use case: Matrix searching, grid processing
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            print(f"Even number {matrix[i][j]} at position ({i},{j})")



#EX 4: For Loop + If with Break (Early Exit)
#---------------------------------------------------
"""
Explanation: Exit loop as soon as condition is met
Use case: Finding first match, search operations
"""
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
target = 'Charlie'

for i, student in enumerate(students):
    if student == target:
        print(f"Found {target} at index {i}")
        break
else:
    print(f"{target} not found")



#EX 5: For Loop + If with Continue (Skip Items)
#---------------------------------------------------
"""
Explanation: Skip certain items and continue processing others
Use case: Filtering out unwanted values, error handling
"""
prices = [10, -5, 20, 0, 15, -3, 25]

total = 0
for price in prices:
    if price <= 0:
        print(f"Skipping invalid price: {price}")
        continue
    
    total += price
    print(f"Added {price}, running total: {total}")

print(f"Final total: {total}")



#EX 6: While Loop + If/Else (Input Validation)
#---------------------------------------------------
"""
Explanation: Validate input inside while loop with if/else
Use case: User input validation, retry logic
"""
while True:
    age = input("Enter your age (or 'q' to quit): ")
    
    if age.lower() == 'q':
        print("Exiting...")
        break
    
    if not age.isdigit():
        print("❌ Please enter a valid number!")
        continue
    
    age = int(age)
    
    if age < 0:
        print("❌ Age cannot be negative!")
    elif age < 18:
        print("🚫 You are a minor")
    elif age < 65:
        print("✅ You are an adult")
    else:
        print("👴 You are a senior")
    
    break



#EX 7: While Loop + Nested If (Complex Conditions)
#---------------------------------------------------
"""
Explanation: Multiple nested conditions for complex decision making
Use case: Game logic, state machines, workflow processing
"""
health = 100
energy = 50

while health > 0:
    print(f"\nHealth: {health}, Energy: {energy}")
    action = input("Action (attack/rest/quit): ").lower()
    
    if action == 'attack':
        if energy >= 10:
            print("⚔️ Attack successful!")
            energy -= 10
            health -= 5  # Enemy counter-attack
        else:
            print("❌ Not enough energy!")
    
    elif action == 'rest':
        if energy < 100:
            energy = min(100, energy + 20)
            print(f"😴 Rested. Energy: {energy}")
        else:
            print("Already at full energy!")
    
    elif action == 'quit':
        print("Game ended!")
        break
    
    else:
        print("Invalid action!")
    
    if health <= 0:
        print("💀 You died!")



#EX 8: For Loop + While Loop (Nested Mixed Loops)
#---------------------------------------------------
"""
Explanation: For loop containing while loop (or vice versa)
Use case: Processing batches with retry logic
"""
tasks = ['Task1', 'Task2', 'Task3']

for task in tasks:
    print(f"\n📋 Processing {task}")
    attempts = 0
    max_attempts = 3
    success = False
    
    while attempts < max_attempts and not success:
        result = input(f"Complete {task}? (yes/no): ").lower()
        
        if result == 'yes':
            print(f"✅ {task} completed!")
            success = True
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"⚠️ Retry {attempts}/{max_attempts}")
            else:
                print(f"❌ {task} failed after {max_attempts} attempts")



#EX 9: List Comprehension + If (Compact Filtering)
#---------------------------------------------------
"""
Explanation: Single-line for loop with conditional
Use case: Quick filtering and transformation
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional way
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Traditional: {evens}")

# Compact way (list comprehension)
evens_compact = [num for num in numbers if num % 2 == 0]
print(f"Compact: {evens_compact}")



#EX 10: List Comprehension + If/Else (Conditional Mapping)
#---------------------------------------------------
"""
Explanation: Transform items differently based on condition
Use case: Data transformation, categorization
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# If/else inside list comprehension (ternary operator)
result = ['EVEN' if num % 2 == 0 else 'ODD' for num in numbers]
print(result)

# More complex: square evens, cube odds
transformed = [num**2 if num % 2 == 0 else num**3 for num in numbers]
print(f"Transformed: {transformed}")



#EX 11: While Loop + Multiple Breaks (Multi-Exit Points)
#---------------------------------------------------
"""
Explanation: Loop with several exit conditions
Use case: Complex state management, game loops
"""
inventory = ['apple', 'sword', 'potion']
gold = 50

while True:
    print(f"\n💰 Gold: {gold}")
    print(f"🎒 Inventory: {inventory}")
    
    action = input("Action (buy/sell/check/quit): ").lower()
    
    if action == 'buy':
        item = input("Item to buy (potion=10g, sword=30g): ").lower()
        
        if item == 'potion' and gold >= 10:
            inventory.append('potion')
            gold -= 10
            print("✅ Bought potion!")
        elif item == 'sword' and gold >= 30:
            inventory.append('sword')
            gold -= 30
            print("✅ Bought sword!")
        else:
            print("❌ Not enough gold!")
    
    elif action == 'sell':
        if len(inventory) == 0:
            print("❌ Nothing to sell!")
        else:
            item = input(f"Sell which item? {inventory}: ").lower()
            if item in inventory:
                inventory.remove(item)
                gold += 5
                print(f"✅ Sold {item} for 5g!")
    
    elif action == 'check':
        if gold <= 0:
            print("💀 You're broke! Game Over!")
            break
    
    elif action == 'quit':
        print("👋 Thanks for playing!")
        break
    
    else:
        print("Invalid action!")



#EX 12: For-Else + While (Combination Pattern)
#---------------------------------------------------
"""
Explanation: For loop with else clause, containing while loop
Use case: Search with fallback, nested retry logic
"""
users = ['admin', 'user1', 'user2']
target_user = 'admin'

for user in users:
    if user == target_user:
        print(f"🔍 Found {target_user}!")
        
        # Nested authentication attempts
        attempts = 0
        while attempts < 3:
            password = input("Enter password: ")
            
            if password == 'secret':
                print("✅ Access granted!")
                break
            else:
                attempts += 1
                print(f"❌ Wrong password. {3 - attempts} attempts left.")
        else:
            print("🔒 Account locked!")
        
        break
else:
    print(f"❌ User {target_user} not found!")
from helper import br, ctitle

# 💪 Built-In Functions in Python

# # print(dir(str)) 
# for i in dir(str):
#     print('{} ,'.format(i))




# materials = ["Concrete", "steel", "glass", "wood", "brick"]

# # """
# count = 0
# for mat in materials:
#     count += 1
#     print(count, mat)

# (base) PS C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic> python .\20_Functions_BuiltInFunction_02.py
# 1 Concrete
# 2 steel
# 3 glass
# 4 wood
# 5 brick
# """

# for n, mat in enumerate(materials, 1):
#     print(n, mat)



# # isinstance()

# x = 42
# y = "hello"
# z = [1,2,3]

# print(isinstance(x, int))
# print(isinstance(y,str))
# print(isinstance(z,list))
# print(isinstance(z,dict))

# if isinstance(x, int):
#     print(x**2)
#     print(x*x)


# Dictionary with material names as keys and prices/costs as values
material = {'steel'     : 120,
            'Concrete'  : 75,
            'Wood'      : 40,
            'Brick'     : 95} 

# Define a function to extract the value (second element) from a key-value tuple
# When sorting dictionaries, items() returns tuples like ('steel', 120)
# item[0] = key (material name), item[1] = value (price)
def get_value(item):
    return item[1]  # Return the price/value for sorting

# Sort the dictionary by VALUES (prices) in ascending order
# material.items() converts dict to list of tuples: [('steel', 120), ('Concrete', 75), ...]
# key=get_value tells sorted() to use the price (second element) for comparison
# Result: sorted from lowest to highest price
sorted_materials = sorted(material.items(), key=get_value)
print(sorted_materials)
# Output: [('Wood', 40), ('Concrete', 75), ('Brick', 95), ('steel', 120)]

print("\n" + "="*60)
print("SIMPLIFIED EXAMPLE - Sort students by age")
print("="*60 + "\n")

# Simple dictionary: student names and their ages
students = {'Alice': 25, 'Bob': 20, 'Charlie': 23}

# Function to get age (the value)
def get_age(student):
    return student[1]  # student is a tuple like ('Alice', 25)

# Sort students by age (youngest to oldest)
sorted_students = sorted(students.items(), key=get_age)
print("Sorted by age:", sorted_students)
# Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

print("\n" + "-"*60)
print("EVEN SIMPLER - Using lambda (no need for separate function)")
print("-"*60 + "\n")

# Same result using lambda function (one line!)
sorted_students2 = sorted(students.items(), key=lambda x: x[1])
print("Sorted by age:", sorted_students2)
# Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

print("\n" + "-"*60)
print("Sort by NAME instead (alphabetically)")
print("-"*60 + "\n")

# Sort by key (name) instead of value (age)
sorted_by_name = sorted(students.items(), key=lambda x: x[0])
print("Sorted by name:", sorted_by_name)
# Output: [('Alice', 25), ('Bob', 20), ('Charlie', 23)]



# Zip function
new_materials = material
print(f"{new_materials} <---")
# ============================================================================
# COMPREHENSION IN PYTHON - Complete Guide
# ============================================================================
"""
Comprehensions create concise, readable one-liners for creating lists, 
dictionaries, sets, and conditional expressions in Python.
"""

from helper import br

# ============================================================================
# 1️⃣ TERNARY OPERATOR (Conditional Expression)
# ============================================================================
"""
Syntax: value_if_true if condition else value_if_false

Traditional:
    if toggle == True:
        word = 'Enabled'
    else:
        word = 'Disabled'

Comprehension:
    word = 'Enabled' if toggle else 'Disabled'
"""

print("=" * 70)
print("1️⃣ TERNARY OPERATOR EXAMPLES")
print("=" * 70)

# Example 1: Toggle state
toggle = True
word = 'Enabled' if toggle else 'Disabled'
print(f"Toggle is: {word}")

# Example 2: Age check
age = 25
status = 'Adult' if age >= 18 else 'Minor'
print(f"Age {age}: {status}")

# Example 3: Grade assignment
score = 85
grade = 'Pass' if score >= 60 else 'Fail'
print(f"Score {score}: {grade}")

# Example 4: Nested ternary (not recommended for complex logic)
num = 0
result = 'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'
print(f"Number {num}: {result}")

br(70)


# ============================================================================
# 2️⃣ LIST COMPREHENSION
# ============================================================================
"""
Syntax: [expression for item in iterable if condition]

Parts:
    - expression: What to do with each item
    - for item in iterable: Loop through items
    - if condition: Optional filter (include only if True)
"""

print("2️⃣ LIST COMPREHENSION EXAMPLES")
print("=" * 70)

# Example 1: Original - Convert to uppercase
items = ['item_a', 'item_b', 'item_c', 'item_d', 'Wrong_data']

# Traditional way
upper_items_traditional = []
for item in items:
    upper_items_traditional.append(item.upper())
print("Traditional:", upper_items_traditional)

# Comprehension way
upper_items_comprehension = [item.upper() for item in items]
print("Comprehension:", upper_items_comprehension)

# Example 2: Original - Filtering with condition
items_with_a = [item for item in items if 'a' in item]
print("Items with 'a':", items_with_a)

# Example 3: Original - Filter and transform
upper_items2 = [item.upper() for item in items if 'item_' in item]
print("Filtered & uppercase:", upper_items2)

br(70)


# ============================================================================
# 3️⃣ LIST COMPREHENSION - Number Operations
# ============================================================================
print("3️⃣ NUMBER OPERATIONS WITH LIST COMPREHENSION")
print("=" * 70)

numbers = [1, 2, 3, 4, 5]

# Square numbers
num_sq = [num**2 for num in numbers]
print(f"Numbers:        {numbers}")
print(f"Squares:        {num_sq}")

# Cube numbers
num_cube = [num**3 for num in numbers]
print(f"Cubes:          {num_cube}")

# Even numbers only (cubed)
num_cube_even = [num**3 for num in numbers if num % 2 == 0]  # Fixed: & to %
print(f"Even cubed:     {num_cube_even}")

# Even/Odd labeling
even_odd = ['Even' if num % 2 == 0 else 'Odd' for num in numbers]
print(f"Even/Odd:       {even_odd}")

# Additional examples
doubled = [num * 2 for num in numbers]
print(f"Doubled:        {doubled}")

negative = [-num for num in numbers]
print(f"Negative:       {negative}")

greater_than_2 = [num for num in numbers if num > 2]
print(f"Greater than 2: {greater_than_2}")

br(70)


# ============================================================================
# 4️⃣ LIST COMPREHENSION - String Filtering
# ============================================================================
print("4️⃣ STRING FILTERING EXAMPLES")
print("=" * 70)

mats = ["wood", "steel", "concrete", "bricks", "glass", "Plaster"]

# Filter materials with 'w'
mats_with_w = [mat for mat in mats if 'w' in mat.lower()]
print(f"Materials with 'w': {mats_with_w}")

# Filter by length
long_mats = [mat for mat in mats if len(mat) > 5]
print(f"Long names (>5):    {long_mats}")

# Capitalize all
capitalized = [mat.capitalize() for mat in mats]
print(f"Capitalized:        {capitalized}")

# Filter and transform
uppercase_w = [mat.upper() for mat in mats if 'w' in mat.lower()]
print(f"Uppercase with 'w': {uppercase_w}")

br(70)


# ============================================================================
# 5️⃣ DICTIONARY COMPREHENSION
# ============================================================================
"""
Syntax: {key_expression: value_expression for item in iterable if condition}
"""

print("5️⃣ DICTIONARY COMPREHENSION EXAMPLES")
print("=" * 70)

# Example 1: Original - lowercase keys, uppercase values
mats = ["wood", "steel", "concrete", "bricks", "glass", "Plaster"]
dict_mats = {mat.lower(): mat.upper() for mat in mats}
print("Material dict:")
for key, value in dict_mats.items():
    print(f"  {key:12} → {value}")

# Example 2: Number to square mapping
num_dict = {num: num**2 for num in range(1, 6)}
print(f"\nNumber squares: {num_dict}")

# Example 3: String length mapping
word_lengths = {word: len(word) for word in ['apple', 'banana', 'cherry']}
print(f"Word lengths:   {word_lengths}")

# Example 4: Conditional dictionary
even_squares = {num: num**2 for num in range(1, 11) if num % 2 == 0}
print(f"Even squares:   {even_squares}")

# Example 5: Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in original.items()}
print(f"Original:       {original}")
print(f"Swapped:        {swapped}")

br(70)


# ============================================================================
# 6️⃣ SET COMPREHENSION
# ============================================================================
"""
Syntax: {expression for item in iterable if condition}
Note: Uses {} like dict, but only expression (no key:value)
"""

print("6️⃣ SET COMPREHENSION EXAMPLES")
print("=" * 70)

# Example 1: Unique squares
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
unique_squares = {num**2 for num in numbers}
print(f"Numbers:        {numbers}")
print(f"Unique squares: {unique_squares}")

# Example 2: Unique lengths
words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'ant']
lengths = {len(word) for word in words}
print(f"Words:          {words}")
print(f"Unique lengths: {sorted(lengths)}")

# Example 3: First letters (unique)
first_letters = {word[0].upper() for word in words}
print(f"First letters:  {sorted(first_letters)}")

br(70)


# ============================================================================
# 7️⃣ NESTED COMPREHENSION
# ============================================================================
print("7️⃣ NESTED COMPREHENSION EXAMPLES")
print("=" * 70)

# Example 1: Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix:     {matrix}")
print(f"Flattened:  {flattened}")

# Example 2: Create multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("\nMultiplication table:")
for row in mult_table:
    print(row)

# Example 3: Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(f"\nProduct combinations: {combinations}")

br(70)


# ============================================================================
# 8️⃣ COMPREHENSION COMPARISON SUMMARY
# ============================================================================
print("8️⃣ COMPREHENSION TYPES SUMMARY")
print("=" * 70)

data = [1, 2, 3, 4, 5]

print("List comprehension:   ", [x**2 for x in data])
print("Set comprehension:    ", {x**2 for x in data})
print("Dict comprehension:   ", {x: x**2 for x in data})
print("Generator expression: ", (x**2 for x in data), "← Returns generator object")

print("\n" + "=" * 70)
print("✅ Comprehension examples completed!")
print("=" * 70)
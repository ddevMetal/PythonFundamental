# Collection Data Types in Python (List, Tuple, Set, Dictionary)
#----------------------------------------------------------------------
# List       |               | Mutable   | Ordered   | Collection     |
# Tuple      |               | Immutable | Ordered   | Collection     |
# Set        | Unique        | Mutable   | Unordered | Collection     |
# Dictionary | Mapped        | Mutable   | Ordered*  | Collection     |
#


# mutable -> can be changed
# immutable -> cannot be changed


# ============================================
# LIST
# ============================================

empty_list = []
house_parts = ['Wall', 'Floor', 'Roof', 'Ceiling', 'Wall', 'Floor', 'Roof', 'Ceiling', 'Wall', 'Floor', 'Roof', 'Ceiling']     


# ============================================
# Get Single List Item
# ============================================

print("Single Item Access:")
print(house_parts[0])     # First Item (index starts from 0)
print(house_parts[2])     # Third Item (index 2)
print(house_parts[-1])    # Last Item (negative index from end)
print(house_parts[-2])    # Second Last Item
print()


# ============================================
# Get Multiple List Items (Slicing)
# ============================================

print("List Slicing:")
print(house_parts[:2])      # Get until 2nd item (excluding index 2)
print(house_parts[2:])      # Get from 2nd item (including index 2)
print(house_parts[1:3])     # Get from index 1 (including) to 3 (excluding)
print(house_parts[::2])     # Get every second item
print(house_parts[2:6:2])   # Get every 2nd item from index 2 to 6
print(house_parts[::-1])    # Get all items in reverse order
print()


# ============================================
# Slicing Use-case Example: Separate Header from Data
# ============================================

categories = ['Categories', 'Wall', 'Floor', 'Roof', 'Ceiling']

header = categories[0]      # Extract first item as header
data = categories[1:]       # Extract remaining items as data
print("Header:", header)
print("Data:", data)
print()


# ============================================
# Membership Operator (Checking if Item Exists)
# ============================================

print("Membership Check:")
print('Wall' in house_parts)        # True - 'Wall' exists in list
print('Wall' not in house_parts)    # False - 'Wall' does exist
print()


# ============================================
# Common List Functions
# ============================================

numbers = [5, 6, 213, 23, 1, 46, 6]

print("List Functions:")
print("Length:", len(categories))              # Number of items
print("Sorted:", sorted(categories))           # Returns sorted copy (doesn't modify original)
print("Sum:", sum(numbers))                    # Sum of all numbers
print("Min:", min(numbers))                    # Smallest number
print("Max:", max(numbers))                    # Largest number
print()


# ============================================
# List Methods: Adding Items
# ============================================

building_items = ['Wall', 'Floor', 'Roof', 'Ceiling', 'floor']
building_items.append('Window')         # Add single item to end
building_items.append('Door')
print("After append:", building_items)
print()

# Joining lists (3 different methods)
building_items += ['Joint_1', 'Joint_2']       # Method 1: += operator
building_items.extend(house_parts)             # Method 2: extend() method
combined_list = house_parts + building_items   # Method 3: + operator (creates new list)
print("After joining:", building_items)
print()


# ============================================
# List Operations: Count Occurrences
# ============================================

floor_count = building_items.count('Floor')
print("Count of 'Floor':", floor_count)
print()


# ============================================
# List Methods: Insert at Specific Position
# ============================================

building_items.insert(6, 'Balcony')
print("After insert at index 6:", building_items)
print()


# ============================================
# List Methods: Remove Items
# ============================================

building_items.remove('Balcony')    # Remove by value (first occurrence)
print("After remove:", building_items)
print()

# Pop - remove and return item by index
removed_item = building_items.pop(3)
print("Popped item at index 3:", removed_item)
print()

# Pop all items safely
print("Popping all items:")
index = 0
while len(building_items) > 0:
    item = building_items.pop(0)    # Always pop from front
    print(f"{item} (position {index})")
    index += 1

print("List length after popping all:", len(building_items))
print()


# ============================================
# Clear List (2 Methods)
# ============================================

# Method 1: clear() method
categories.clear()

# Method 2: assign empty list (recommended - cleaner)
categories = []


# ============================================
# Copy List (Shallow Copy)
# ============================================

original_list = ['one', 'two', 'three', 'four']     # Original list
copied_list = original_list.copy()                  # Independent copy, NOT a reference

original_list.append('five')

print("Original after append:", original_list)      # ['one', 'two', 'three', 'four', 'five']
print("Copy (unchanged):", copied_list)             # ['one', 'two', 'three', 'four']
print()


# ============================================
# Replace Items in List
# ============================================

items = ['item_1', 'item_2', 'item_3', 'item_4']
print("Before replace:", items)

items[2] = 'new_item_3'     # Replace by index
items[-1] = 'new_item_4'    # Replace using negative index
print("After replace:", items)

# Replace using slice
items[:2] = ['first', 'second']     # Replace first 2 items
print("After slice replace:", items)
print()


# ============================================
# Nested Lists (2D Lists)
# ============================================

nested_list = [
    ['one', 'two', 'three'],
    ['four', 'five', 'six'],
    ['seven', 'eight', 'nine']
]

# Access nested items using [row][column]
print("Item at row 1, column 2:", nested_list[1][2])    # 'six'

# Extract entire row
first_row = nested_list[0]
print("First row:", first_row[0], first_row[1], first_row[2])


# ============================================
# FOR LOOPS
# ============================================
myLoopyList = ['A-cup', 'B-Cup', 'C-cup', 'D-cup','E-cup']
for i in myLoopyList:
    print("Tiites Size is: " + i + "!")
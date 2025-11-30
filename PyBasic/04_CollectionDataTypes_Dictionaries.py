# ============================================
# DICTIONARIES - Key-Value Pairs Collection
# ============================================
#
# Key Characteristics:
# - KEY-VALUE PAIRS: Each item has a key and associated value
# - ORDERED: Maintains insertion order (Python 3.7+)
# - MUTABLE: Can add, remove, and modify items
# - UNIQUE KEYS: Keys must be unique (values can duplicate)
# - FAST LOOKUP: Very efficient retrieval by key (O(1) time complexity)
# - KEYS MUST BE IMMUTABLE: Keys can be strings, numbers, tuples (not lists)
# - VALUES CAN BE ANYTHING: Any data type including lists, dicts, objects
#
# Use Cases:
# - Store structured data (user profiles, configuration settings)
# - JSON-like data structures
# - Caching and memoization
# - Counting and grouping (word frequency, category counts)
# - Database-like records
# - API responses and request payloads
# - Mapping relationships (student ID to name, product code to price)
#
# Syntax: {key1: value1, key2: value2, key3: value3}
# Access: dict[key] or dict.get(key, default)
# ============================================


# ============================================
# Creating Dictionaries
# ============================================

empty_dict = {}     # Empty dictionary

# Student profile
student_profile = {
    'name': 'Alice Johnson',
    'age': 22,
    'major': 'Computer Science',
    'gpa': 3.85
}

# Product catalog
product_catalog = {
    'P001': {'name': 'Laptop', 'price': 1299.99, 'stock': 15},
    'P002': {'name': 'Mouse', 'price': 29.99, 'stock': 50},
    'P003': {'name': 'Keyboard', 'price': 79.99, 'stock': 30}
}

# Python data types reference
python_types = {
    'int': 'A whole number, like 1, 2, or 3.',
    'float': 'A number that can have a decimal point, like 2.5 or 0.1.',
    'str': 'Words or letters, like "hello" or "apple".',
    'bool': 'True/False. Similar to Yes/No parameter in Revit.',
    'list': 'A group of things you can change, like [1, 2, "apple"].',
    'tuple': 'A collection of things that you cannot change, like (1, 2, "apple").',
    'dict': 'Pairs of things like {"name": "john", "age": 10}.',
    'set': 'A group of unique things, like {1, 2, 3}. Duplicates are ignored.',
    'NoneType': 'Means nothing or empty, like an empty box.'
}

print("Student Profile:", student_profile)
print()


# ============================================
# Accessing Dictionary Values
# ============================================

# Method 1: Using square brackets [] - raises error if key doesn't exist
print("Student name:", student_profile['name'])
print("Student GPA:", student_profile['gpa'])

# Method 2: Using get() - returns None (or default) if key doesn't exist
print("Student major:", student_profile.get('major'))
print("Student ID:", student_profile.get('id', 'Not assigned'))  # Default value
print()

# Access from nested dictionary
print("Product P001 name:", product_catalog['P001']['name'])
print("Product P002 price:", product_catalog['P002']['price'])
print()


# ============================================
# Adding and Modifying Items
# ============================================

# Add new key-value pair
student_profile['email'] = 'alice.johnson@university.edu'
student_profile['graduation_year'] = 2026

# Modify existing value
student_profile['age'] = 23
student_profile['gpa'] = 3.90

print("Updated student profile:", student_profile)
print()

# Using setdefault() - adds key only if it doesn't exist
student_profile.setdefault('advisor', 'Dr. Smith')  # Adds new key
student_profile.setdefault('name', 'Unknown')       # Doesn't change existing
print("After setdefault:", student_profile)
print()


# ============================================
# Membership Operators (Checking Keys)
# ============================================

print("Membership checks:")
print("'name' in student_profile:", 'name' in student_profile)          # True
print("'phone' in student_profile:", 'phone' in student_profile)        # False
print("'email' not in student_profile:", 'email' not in student_profile)  # False
print()


# ============================================
# Dictionary Methods
# ============================================

# Get all keys
all_keys = list(python_types.keys())
print("All Python type keys:", all_keys)
print()

# Get all values
all_values = list(python_types.values())
print("All Python type descriptions:", all_values)
print()

# Get all key-value pairs as tuples
all_items = list(python_types.items())
print("All items (key-value tuples):")
for key, value in all_items[:3]:  # Show first 3
    print(f"  {key}: {value}")
print()


# ============================================
# Merging Dictionaries
# ============================================

# Additional student information
additional_info = {
    'phone': '555-1234',
    'address': '123 Campus Drive',
    'emergency_contact': 'John Johnson'
}

# Method 1: update() - modifies original dictionary
student_profile.update(additional_info)
print("After update:", student_profile)
print()

# Method 2: Merge operator | (Python 3.9+)
contact_info = {'email': 'alice@email.com', 'linkedin': 'linkedin.com/alice'}
emergency_info = {'emergency_phone': '555-9999', 'medical_info': 'None'}
full_contact = contact_info | emergency_info
print("Merged using |:", full_contact)
print()


# ============================================
# Removing Items
# ============================================

# Create a copy for demonstration
temp_dict = student_profile.copy()

# pop() - remove and return value
removed_phone = temp_dict.pop('phone')
print(f"Removed phone: {removed_phone}")
print("After pop:", temp_dict.keys())

# pop() with default (no error if key doesn't exist)
removed_item = temp_dict.pop('nonexistent_key', 'Not found')
print(f"Tried to remove nonexistent key: {removed_item}")

# popitem() - remove and return last inserted key-value pair
last_item = temp_dict.popitem()
print(f"Removed last item: {last_item}")

# del - delete specific key
del temp_dict['address']
print("After del:", temp_dict.keys())

# clear() - remove all items
temp_dict.clear()
print("After clear:", temp_dict)
print()


# ============================================
# Iterating Through Dictionaries
# ============================================

print("=== Iterating Through Dictionaries ===")
print()

# Iterate over keys (default)
print("Product codes:")
for code in product_catalog:
    print(f"  {code}")
print()

# Iterate over values
print("Product details:")
for product in product_catalog.values():
    print(f"  {product['name']} - ${product['price']}")
print()

# Iterate over key-value pairs
print("Full product catalog:")
for code, details in product_catalog.items():
    print(f"  {code}: {details['name']} - ${details['price']} ({details['stock']} in stock)")
print()


# ============================================
# Dictionary Comprehension
# ============================================

# Create dictionary from range
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)

# Filter and transform
prices = {'apple': 1.50, 'banana': 0.75, 'orange': 2.00, 'grape': 3.50}
expensive_fruits = {fruit: price for fruit, price in prices.items() if price > 1.00}
print("Expensive fruits:", expensive_fruits)
print()


# ============================================
# Nested Dictionaries (Complex Data)
# ============================================

# Company organizational structure
company = {
    'Engineering': {
        'manager': 'Alice Smith',
        'employees': ['Bob', 'Carol', 'David'],
        'budget': 500000
    },
    'Marketing': {
        'manager': 'Emma Wilson',
        'employees': ['Frank', 'Grace'],
        'budget': 200000
    },
    'Sales': {
        'manager': 'Henry Brown',
        'employees': ['Iris', 'Jack', 'Kate', 'Leo'],
        'budget': 300000
    }
}

# Access nested data
print("Engineering manager:", company['Engineering']['manager'])
print("Marketing employees:", company['Marketing']['employees'])
print("Sales budget:", company['Sales']['budget'])
print()

# Iterate through nested structure
print("Department budgets:")
for dept, info in company.items():
    print(f"  {dept}: ${info['budget']:,}")
print()


# ============================================
# Common Dictionary Functions
# ============================================

scores = {'math': 95, 'english': 88, 'science': 92, 'history': 85}

print("Dictionary functions:")
print("Number of subjects:", len(scores))
print("Sorted keys:", sorted(scores.keys()))
print("Sorted by values:", sorted(scores.items(), key=lambda x: x[1], reverse=True))
print()


# ============================================
# Practical Use Cases
# ============================================

print("=== PRACTICAL USE CASES ===")
print()

# Use Case 1: Word frequency counter
text = "python is amazing python is powerful python is fun"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)
print()

# Use Case 2: Configuration settings
app_config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'username': 'admin',
        'database_name': 'app_db'
    },
    'api': {
        'base_url': 'https://api.example.com',
        'timeout': 30,
        'retry_count': 3
    },
    'features': {
        'enable_logging': True,
        'enable_cache': True,
        'debug_mode': False
    }
}

print("Database host:", app_config['database']['host'])
print("API timeout:", app_config['api']['timeout'])
print("Debug mode:", app_config['features']['debug_mode'])
print()

# Use Case 3: Grouping data by category
students_by_grade = {}
student_list = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Carol', 'grade': 'A'},
    {'name': 'David', 'grade': 'C'},
    {'name': 'Emma', 'grade': 'B'}
]

for student in student_list:
    grade = student['grade']
    if grade not in students_by_grade:
        students_by_grade[grade] = []
    students_by_grade[grade].append(student['name'])

print("Students grouped by grade:", students_by_grade)
print()


print("=" * 50)
print("✓ Dictionaries Tutorial Complete!")
print("=" * 50)
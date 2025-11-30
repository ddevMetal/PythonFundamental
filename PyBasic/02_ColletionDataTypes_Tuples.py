# ============================================
# TUPLES - Immutable Ordered Collection
# ============================================
#
# Key Characteristics:
# - IMMUTABLE: Cannot be changed after creation (no add, remove, or modify)
# - ORDERED: Items maintain their position
# - ALLOW DUPLICATES: Can contain duplicate values
# - INDEXED: Access items by position [0, 1, 2, ...]
# - FASTER: More memory efficient than lists
# - HASHABLE: Can be used as dictionary keys (lists cannot)
#
# Use Cases:
# - Store data that should never change (coordinates, RGB colors, database records)
# - Dictionary keys (tuples can be keys, lists cannot)
# - Function return multiple values
# - Data integrity (protect against accidental modification)
# - Configuration settings that shouldn't be modified
#
# Syntax: (item1, item2, item3) or item1, item2, item3
# ============================================


# ============================================
# Creating Tuples
# ============================================

empty_tuple = ()
single_item = (42,)  # IMPORTANT: Comma required for single-item tuple!
not_a_tuple = (42)   # This is just an integer, NOT a tuple

# Geographic coordinates (latitude, longitude)
new_york_coords = (40.7128, -74.0060)
london_coords = (51.5074, -0.1278)
tokyo_coords = (35.6762, 139.6503)

# RGB color codes
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)

# Personal information (first_name, last_name, age, employee_id)
employee_1 = ("Alice", "Johnson", 28, "E001")
employee_2 = ("Bob", "Smith", 35, "E002")
employee_3 = ("Carol", "Williams", 42, "E003")

print("Empty tuple:", empty_tuple)
print("Single item tuple:", single_item)
print("NOT a tuple:", not_a_tuple, type(not_a_tuple))
print("\nGeographic Coordinates:")
print(f"New York: {new_york_coords}")
print(f"London: {london_coords}")
print(f"Tokyo: {tokyo_coords}")
print()


# ============================================
# Accessing Tuple Elements
# ============================================

# Unpack employee information
first_name, last_name, age, emp_id = employee_1
print(f"Employee: {first_name} {last_name}, Age: {age}, ID: {emp_id}")

# Access by index
print(f"First name: {employee_2[0]}")
print(f"Employee ID: {employee_2[3]}")
print(f"Last employee: {employee_3[-1]}")  # Negative indexing
print()


# ============================================
# Slicing Tuples
# ============================================

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

work_days = week_days[:5]       # First 5 days
weekend = week_days[5:]         # Last 2 days
mid_week = week_days[2:5]       # Wednesday to Friday

print("Work days:", work_days)
print("Weekend:", weekend)
print("Mid-week:", mid_week)
print()


# ============================================
# Common Tuple Operations
# ============================================

exam_scores = (85, 92, 78, 95, 88, 92, 85, 90)

print("Number of exams:", len(exam_scores))
print("Lowest score:", min(exam_scores))
print("Highest score:", max(exam_scores))
print("Total points:", sum(exam_scores))
print("Average score:", sum(exam_scores) / len(exam_scores))
print("Sorted scores:", sorted(exam_scores))              # Returns list
print("Sorted as tuple:", tuple(sorted(exam_scores)))     # Convert back to tuple
print()


# ============================================
# Tuple Methods (Only 2!)
# ============================================

exam_scores = (85, 92, 78, 95, 88, 92, 85, 90)

# count() - Count occurrences of a value
print("How many times 92 appears:", exam_scores.count(92))     # Returns 2
print("How many times 85 appears:", exam_scores.count(85))     # Returns 2

# index() - Find first position of a value
print("Position of first 92:", exam_scores.index(92))          # Returns 1
print("Position of 95:", exam_scores.index(95))                # Returns 3
print()


# ============================================
# UNIQUE PROPERTY 1: Immutability
# ============================================

print("=== IMMUTABILITY DEMONSTRATION ===")

database_config = ("localhost", 5432, "production_db", "admin")

# This will cause an error - tuples cannot be modified!
try:
    database_config[0] = "192.168.1.100"
except TypeError as e:
    print(f"ERROR: {e}")
    print("✓ Tuples are immutable - cannot change values!")

# To "modify", you must create a new tuple
database_config = ("192.168.1.100", 5432, "production_db", "admin")
print(f"✓ New config created: {database_config}")
print()


# ============================================
# UNIQUE PROPERTY 2: Tuples as Dictionary Keys
# ============================================

print("=== TUPLES AS DICTIONARY KEYS ===")

# Use coordinate tuples as keys (lists would fail here!)
city_locations = {
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo",
    (48.8566, 2.3522): "Paris"
}

# Look up city by coordinates
nyc_coords = (40.7128, -74.0060)
print(f"City at {nyc_coords}: {city_locations[nyc_coords]}")

# This would NOT work with lists:
# city_locations = {[40.7128, -74.0060]: "New York"}  # TypeError!
print("✓ Tuples can be dictionary keys, lists cannot!")
print()


# ============================================
# UNIQUE PROPERTY 3: Memory Efficiency
# ============================================

print("=== MEMORY EFFICIENCY ===")

import sys

# Compare memory usage
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

list_size = sys.getsizeof(list_data)
tuple_size = sys.getsizeof(tuple_data)

print(f"List size: {list_size} bytes")
print(f"Tuple size: {tuple_size} bytes")
print(f"✓ Tuples use {list_size - tuple_size} bytes less memory!")
print()


# ============================================
# UNIQUE PROPERTY 4: Tuple Unpacking
# ============================================

print("=== TUPLE UNPACKING ===")

# Basic unpacking
latitude, longitude = new_york_coords
print(f"NYC Latitude: {latitude}, Longitude: {longitude}")

# Unpacking with * operator (collect remaining items)
first_day, *middle_days, last_day = week_days
print(f"First day: {first_day}")
print(f"Middle days: {middle_days}")
print(f"Last day: {last_day}")

# Swap values using tuple unpacking (Python magic!)
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Swap without temp variable!
print(f"After swap: a={a}, b={b}")
print()


# ============================================
# UNIQUE PROPERTY 5: Returning Multiple Values
# ============================================

print("=== FUNCTION RETURNING MULTIPLE VALUES ===")

def calculate_statistics(numbers):
    """Returns min, max, average as a tuple"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

def get_user_credentials():
    """Simulate fetching user data"""
    return "alice@example.com", "hashed_password_123", "admin"

# Unpack function results
scores = [85, 92, 78, 95, 88]
min_score, max_score, avg_score = calculate_statistics(scores)
print(f"Min: {min_score}, Max: {max_score}, Average: {avg_score:.2f}")

email, password, role = get_user_credentials()
print(f"User: {email}, Role: {role}")
print()


# ============================================
# Nested Tuples (Tuples within Tuples)
# ============================================

print("=== NESTED TUPLES ===")

# Company organizational structure
company_data = (
    ("Engineering", ("Alice", "Bob", "Carol")),
    ("Marketing", ("David", "Emma")),
    ("Sales", ("Frank", "Grace", "Henry", "Iris"))
)

# Access nested data
print(f"First department: {company_data[0][0]}")
print(f"First engineer: {company_data[0][1][0]}")
print(f"All salespeople: {company_data[2][1]}")
print()


# ============================================
# Converting Between Lists and Tuples
# ============================================

print("=== CONVERSION BETWEEN LISTS AND TUPLES ===")

# List to Tuple (when you need immutability)
mutable_scores = [85, 92, 78, 95]
immutable_scores = tuple(mutable_scores)
print(f"List: {mutable_scores} (type: {type(mutable_scores).__name__})")
print(f"Tuple: {immutable_scores} (type: {type(immutable_scores).__name__})")

# Tuple to List (when you need to modify)
final_scores = list(immutable_scores)
final_scores.append(88)  # Now we can modify
print(f"Modified list: {final_scores}")
print()


# ============================================
# Practical Use Case: Configuration Settings
# ============================================

print("=== PRACTICAL USE CASE ===")

# Database configuration (should never change during runtime)
DB_CONFIG = ("localhost", 5432, "app_database", "readonly_user", "secure_password")

# API endpoints (fixed URLs)
API_ENDPOINTS = (
    "https://api.example.com/users",
    "https://api.example.com/products",
    "https://api.example.com/orders"
)

# Application version (semantic versioning)
APP_VERSION = (2, 1, 5)  # Major, Minor, Patch

host, port, db_name, user, password = DB_CONFIG
print(f"Connecting to {db_name} at {host}:{port}")
print(f"Application version: {APP_VERSION[0]}.{APP_VERSION[1]}.{APP_VERSION[2]}")
print()


print("=" * 50)
print("✓ Tutorial Complete!")
print("=" * 50)



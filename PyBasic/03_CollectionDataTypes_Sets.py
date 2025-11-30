# ============================================
# SETS - Unordered Collection of Unique Items
# ============================================
#
# Key Characteristics:
# - UNIQUE: Automatically removes duplicate values
# - UNORDERED: No index, no guaranteed order
# - MUTABLE: Can add/remove items (but items themselves must be immutable)
# - NO INDEXING: Cannot access by position [0], [1], etc.
# - FAST LOOKUP: Very efficient for membership testing (in operator)
# - MATHEMATICAL OPERATIONS: Union, intersection, difference, symmetric difference
#
# Use Cases:
# - Remove duplicates from a list
# - Membership testing (check if item exists)
# - Mathematical set operations (find common items, unique items, etc.)
# - Tag systems, category management
# - Finding unique visitors, unique words in text
# - Data deduplication
#
# Syntax: {item1, item2, item3} or set([item1, item2, item3])
# Note: {} creates an empty dictionary, NOT a set. Use set() for empty set.
# ============================================

empty_set = set()           # Correct way to create empty set
# empty_set = {}            # WRONG! This creates a dictionary, not a set

# Set automatically removes duplicates
employee_ids = {101, 102, 103, 101, 102, 104, 105, 103}
print("Employee IDs (duplicates removed):", employee_ids)

# Mixed data types
mixed_set = {10, 20, 30, 'Python', 'Java', 'Python', True, False, True}
print("Mixed set:", mixed_set)
print()


# ============================================
# Converting List to Set (Remove Duplicates)
# ============================================

# Website visitor IDs with duplicates
visitor_ids = [1001, 1002, 1003, 1001, 1004, 1002, 1005, 1003, 1001]
print("Visitor IDs (with duplicates):", visitor_ids)

# Convert to set to get unique visitors
unique_visitors = set(visitor_ids)
print("Unique visitors:", unique_visitors)

# Convert back to list if needed
unique_visitor_list = list(unique_visitors)
print("Unique visitors as list:", unique_visitor_list)
print()


# ============================================
# Adding and Removing Items
# ============================================

skills = {'Python', 'JavaScript', 'SQL'}
print("Initial skills:", skills)

# Add single item
skills.add('Docker')
skills.add('Kubernetes')
print("After adding skills:", skills)

# Add multiple items
skills.update(['AWS', 'Azure', 'GCP'])
print("After update:", skills)

# Remove item (raises error if not found)
skills.remove('SQL')
print("After remove:", skills)

# Discard item (no error if not found)
skills.discard('NonExistent')  # No error
print("After discard (no change):", skills)

# Pop (remove random item)
removed_skill = skills.pop()
print(f"Popped skill: {removed_skill}")
print("After pop:", skills)

# Copy and clear
skills_copy = skills.copy()
skills_copy.clear()
print("After clear:", skills_copy)
print()


# ============================================
# Set Mathematical Operations
# ============================================

# Team A skills
team_a_skills = {'Python', 'JavaScript', 'Docker', 'AWS', 'MongoDB'}

# Team B skills
team_b_skills = {'Java', 'JavaScript', 'Kubernetes', 'AWS', 'PostgreSQL'}

print("Team A Skills:", team_a_skills)
print("Team B Skills:", team_b_skills)
print()


# ============================================
# 1. UNION - Combine all items from both sets
# ============================================
# Visual: [A] + [B] = All items from both circles

all_skills = team_a_skills.union(team_b_skills)
# Alternative: all_skills = team_a_skills | team_b_skills
print("UNION - All skills across both teams:")
print(all_skills)
print()


# ============================================
# 2. INTERSECTION - Find common items
# ============================================
# Visual: [A] ∩ [B] = Only the overlapping part

common_skills = team_a_skills.intersection(team_b_skills)
# Alternative: common_skills = team_a_skills & team_b_skills
print("INTERSECTION - Skills both teams have:")
print(common_skills)
print()


# ============================================
# 3. DIFFERENCE - Items in A but not in B
# ============================================
# Visual: [A] - [B] = Orange part of A only

team_a_unique = team_a_skills.difference(team_b_skills)
# Alternative: team_a_unique = team_a_skills - team_b_skills
print("DIFFERENCE - Skills unique to Team A:")
print(team_a_unique)

team_b_unique = team_b_skills.difference(team_a_skills)
print("DIFFERENCE - Skills unique to Team B:")
print(team_b_unique)
print()


# ============================================
# 4. SYMMETRIC DIFFERENCE - Items in A or B but not both
# ============================================
# Visual: [A] △ [B] = Both orange parts (not the overlap)

unique_to_each = team_a_skills.symmetric_difference(team_b_skills)
# Alternative: unique_to_each = team_a_skills ^ team_b_skills
print("SYMMETRIC DIFFERENCE - Skills unique to each team (not shared):")
print(unique_to_each)
print()


# ============================================
# Set Comparison Methods
# ============================================

# Check if one set is subset/superset of another
python_devs = {'Alice', 'Bob', 'Carol'}
all_developers = {'Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank'}
backend_devs = {'Alice', 'Bob', 'Grace'}

print("Python devs:", python_devs)
print("All developers:", all_developers)
print("Backend devs:", backend_devs)
print()


# ============================================
# ISSUBSET - Is A completely inside B?
# ============================================
# Visual: Small circle A inside larger circle B

is_subset = python_devs.issubset(all_developers)
print(f"Are Python devs a subset of all devs? {is_subset}")  # True

is_subset2 = backend_devs.issubset(all_developers)
print(f"Are Backend devs a subset of all devs? {is_subset2}")  # False (Grace not in all_devs)
print()


# ============================================
# ISSUPERSET - Does A contain all items from B?
# ============================================
# Visual: Large circle A contains smaller circle B

is_superset = all_developers.issuperset(python_devs)
print(f"Does all devs contain all Python devs? {is_superset}")  # True

is_superset2 = all_developers.issuperset(backend_devs)
print(f"Does all devs contain all Backend devs? {is_superset2}")  # False (Grace not in all_devs)
print()


# ============================================
# ISDISJOINT - Do sets have NO common items?
# ============================================

frontend_tech = {'React', 'Vue', 'Angular', 'HTML', 'CSS'}
backend_tech = {'Django', 'Flask', 'Node.js', 'Express'}
fullstack_tech = {'React', 'Node.js', 'MongoDB'}

are_disjoint = frontend_tech.isdisjoint(backend_tech)
print(f"Frontend and Backend tech are completely separate? {are_disjoint}")  # True

are_disjoint2 = frontend_tech.isdisjoint(fullstack_tech)
print(f"Frontend and Fullstack tech are completely separate? {are_disjoint2}")  # False (React is common)
print()


# ============================================
# Common Set Functions
# ============================================

number_set = {5, 10, 15, 20, 25, 30, 35}

print("Number set:", number_set)
print("Length:", len(number_set))
print("Minimum:", min(number_set))
print("Maximum:", max(number_set))
print("Sum:", sum(number_set))
print("Sorted (returns list):", sorted(number_set))
print()


# ============================================
# Practical Use Cases
# ============================================

print("=== PRACTICAL USE CASES ===")
print()

# Use Case 1: Email subscription management
subscribed_to_newsletter = {'alice@example.com', 'bob@example.com', 'carol@example.com'}
subscribed_to_promotions = {'bob@example.com', 'david@example.com', 'emma@example.com'}

# Find users subscribed to both
both_subscriptions = subscribed_to_newsletter & subscribed_to_promotions
print("Subscribed to both:", both_subscriptions)

# Find all unique subscribers
all_subscribers = subscribed_to_newsletter | subscribed_to_promotions
print("All unique subscribers:", all_subscribers)
print()


# Use Case 2: Tag-based filtering
post_1_tags = {'python', 'programming', 'tutorial', 'beginner'}
post_2_tags = {'python', 'data-science', 'machine-learning'}
post_3_tags = {'javascript', 'web-development', 'tutorial'}

# Find common tags between posts
common_tags = post_1_tags & post_3_tags
print("Common tags between post 1 and 3:", common_tags)
print()


# Use Case 3: Access control
admin_users = {'admin', 'superuser', 'manager'}
editor_users = {'editor1', 'editor2', 'manager'}
viewer_users = {'viewer1', 'viewer2', 'viewer3'}

# Users with editing rights (admin or editor)
can_edit = admin_users | editor_users
print("Users who can edit:", can_edit)

# Users who are only viewers (not admin or editor)
only_viewers = viewer_users - (admin_users | editor_users)
print("Users who can only view:", only_viewers)
print()


print("=" * 50)
print("✓ Sets Tutorial Complete!")
print("=" * 50)


"""
Context Manager - Timing Execution Example

Context managers help manage resources and execute code before/after a block.
The @contextlib.contextmanager decorator makes it easy to create custom context managers.

Key concepts:
1. Code before 'yield' runs when entering the context (setup)
2. Code after 'yield' runs when exiting the context (cleanup)
3. Context managers ensure cleanup happens even if errors occur
"""

import contextlib
import time

# EX 1: Without context manager (manual timing)
# This approach is verbose and error-prone - you must remember to calculate time after each block
print("=== Example 1: Manual Timing (Without Context Manager) ===")
start = time.time()
manual_result = []
for i in range(100000):
    manual_result.append(i * 2)
end = time.time()
print(f'Manual timing: {end - start:.4f} seconds\n')


# EX 2: With context manager using @contextlib.contextmanager decorator
# This is cleaner, reusable, and automatically handles the timing logic

@contextlib.contextmanager
def time_it(label="Operation"):
    """
    A context manager that times the execution of a code block.
    
    Args:
        label: A descriptive name for the operation being timed
        
    How it works:
    1. Records start time before 'yield'
    2. Yields control back to the with block (your code runs here)
    3. Records end time after your code completes
    4. Calculates and prints the elapsed time
    """
    print(f"[{label}] Starting...")
    start = time.time()
    
    yield  # Your code block executes here
    
    end = time.time()
    elapsed = end - start
    print(f"[{label}] Completed in {elapsed:.4f} seconds")
    print(f"[{label}] That's {elapsed * 1000:.2f} milliseconds\n")


# EX 3: Using the context manager with a loop
print("=== Example 2: Loop with .append() ===")
with time_it("Loop with append"):
    result_loop = []
    for i in range(100000):
        result_loop.append(i * 2)


# EX 4: Using the context manager with list comprehension
# List comprehensions are typically faster than loops with append
print("=== Example 3: List Comprehension ===")
with time_it("List comprehension"):
    result_comp = [i * 2 for i in range(100000)]


# EX 5: Compare different approaches side by side
print("=== Example 4: Performance Comparison ===")

# Method 1: Loop with append
with time_it("Method 1 - Loop + append (100k items)"):
    method1 = []
    for i in range(100000):
        method1.append(i * 2)

# Method 2: List comprehension
with time_it("Method 2 - List comprehension (100k items)"):
    method2 = [i * 2 for i in range(100000)]

# Method 3: Using map function
with time_it("Method 3 - Map function (100k items)"):
    method3 = list(map(lambda x: x * 2, range(100000)))

print("💡 Notice: List comprehensions are usually faster than loops!")
print("💡 Context managers make it easy to time any code block consistently.")
    
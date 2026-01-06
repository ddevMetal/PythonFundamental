"""
Context Manager - Error Handling Example

This demonstrates how context managers can be used to handle exceptions gracefully.
The try_except context manager catches errors and optionally shows debug information.
"""

import contextlib
import time
import traceback

# Example 3: Using try-catch block with context manager

# Context Manager - Timing Code Execution
#----------------------------------------------------------
@contextlib.contextmanager
def time_it():
    start = time.time()
    yield
    end = time.time()
    print(f'Elapsed time: {end - start:.2f}s')


@contextlib.contextmanager
def try_except(debug=False):
    """
    A context manager that catches exceptions and optionally prints debug info.
    
    Args:
        debug: If True, prints the full traceback. If False, prints a simple error message.
    """
    try:
        yield
    except Exception as e:
        if debug:
            print(f"❌ Error occurred: {type(e).__name__}: {e}")
            print("Full traceback:")
            traceback.print_exc()
        else:
            print(f"❌ Error occurred: {type(e).__name__}: {e}")


# Example 1: With debug=True (shows full traceback)
print("=== Example 1: With debug=True ===")
with try_except(debug=True):
    print(1/0)

print()

# Example 2: Without debug (simple error message)
print("=== Example 2: Without debug ===")
with try_except():
    print(1/0)

print()

# Example 3: Different types of errors
print("=== Example 3: Different error types ===")

with try_except(debug=True):
    undefined_variable

print()

with try_except():
    int("not a number")

print()

with try_except(debug=True):
    my_list = [1, 2, 3]
    print(my_list[10])

print()

# Example 4: Code that doesn't raise an error
print("=== Example 4: Successful execution ===")
with try_except():
    result = 10 / 2
    print(f"✅ Success! Result: {result}")

print()

# Example 5: Combining with timing
print("=== Example 5: Combining error handling with timing ===")
with try_except(debug=False):
    with time_it():
        # Simulate some work
        total = sum(range(1000000))
        print(f"✅ Calculated sum: {total}")

print("\n💡 Context managers make error handling clean and reusable!")
    
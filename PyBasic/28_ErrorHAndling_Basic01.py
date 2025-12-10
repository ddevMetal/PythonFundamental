# ERROR Handling in Python

try:
    x = x
    # print(1/0)  # This will raise ZeroDivisionError
    # print('Hello')  # This line will NOT execute
except ZeroDivisionError:
    print('Dividing by 0 is not allowed!')

except:
    print('** ERROR HAPPENED **')
    # import traceback
    # print(traceback.format_exc())

print('End')
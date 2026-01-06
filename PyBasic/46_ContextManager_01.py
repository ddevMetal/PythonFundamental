"""
Context Manager - conept that includes custom functionality before and after your main code block...

by using the 'with' keyword to create a context for your code block.
"""
import contextlib

# decorator : is a function that modifies the behavior of another function without chganging its code.
@contextlib.contextmanager  

def ef_context_manager(): 
    print('---Before---')
    print('---Before---')
    print('---Before---')
    print('---Before---')
    print('---Before---')
    # code before
        
    yield   
    
    # code after
    print('---After---')
    print('---After---')
    print('---After---')
    print('---After---')
    
    
# to use this context manager
# replace the yield
with ef_context_manager():
    print('Inside the context manager')
    for i in range(5):
        print(f'Count: {i+1} inside the context manager')
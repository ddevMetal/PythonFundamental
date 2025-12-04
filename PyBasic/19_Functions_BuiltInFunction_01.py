from helper import br, ctitle

# Built In Function

"""
# A
abs()           : Returns the absolute value of a number | abs(-5) → 5
aiter()         : Returns an asynchronous iterator for an async iterable | aiter(async_obj)
all()           : Returns True if all elements in iterable are true | all([1, 2, 3]) → True
any()           : Returns True if any element in iterable is true | any([0, 1, 0]) → True
anext()         : Returns the next item from async iterator | anext(async_iter)
ascii()         : Returns a string with non-ASCII characters escaped | ascii('café') → "'caf\\xe9'"

# B
bin()           : Converts an integer to binary string | bin(10) → '0b1010'
bool()          : Converts a value to Boolean | bool(0) → False, bool(1) → True
breakpoint()    : Drops into debugger at call site | breakpoint()
bytearray()     : Returns a mutable array of bytes | bytearray([65, 66, 67]) → bytearray(b'ABC')
bytes()         : Returns an immutable bytes object | bytes([65, 66, 67]) → b'ABC'

# C
callable()      : Returns True if object is callable | callable(print) → True
chr()           : Returns character from Unicode code point | chr(65) → 'A'
classmethod()   : Converts method to class method | @classmethod
compile()       : Compiles source into code object | compile('print(1)', '', 'exec')
complex()       : Creates a complex number | complex(1, 2) → (1+2j)

# D
delattr()       : Deletes attribute from object | delattr(obj, 'name')
dict()          : Creates a dictionary | dict(a=1, b=2) → {'a': 1, 'b': 2}
dir()           : Returns list of object's attributes | dir([]) → list methods
divmod()        : Returns quotient and remainder | divmod(10, 3) → (3, 1)

# E
enumerate()     : Returns enumerate object (index, value) | enumerate(['a', 'b']) → [(0,'a'), (1,'b')]
eval()          : Evaluates Python expression from string | eval('2 + 2') → 4
exec()          : Executes Python code dynamically | exec('x = 5')

# F
filter()        : Filters iterable with function | filter(lambda x: x>0, [-1,0,1]) → [1]
float()         : Converts to floating point number | float('3.14') → 3.14
format()        : Formats a value using format spec | format(123.456, '.2f') → '123.46'
frozenset()     : Returns immutable set | frozenset([1, 2, 3])

# G
getattr()       : Gets attribute value from object | getattr(obj, 'name', default)
globals()       : Returns dictionary of global symbol table | globals()

# H
hasattr()       : Returns True if object has attribute | hasattr(obj, 'name')
hash()          : Returns hash value of object | hash('hello')
help()          : Invokes built-in help system | help(print)
hex()           : Converts integer to hexadecimal string | hex(255) → '0xff'

# I
id()            : Returns unique identifier of object | id(x)
input()         : Reads a line from input | name = input('Enter name: ')
int()           : Converts to integer | int('42') → 42, int(3.14) → 3
isinstance()    : Checks if object is instance of class | isinstance(5, int) → True
issubclass()    : Checks if class is subclass | issubclass(bool, int) → True
iter()          : Returns iterator object | iter([1, 2, 3])

# L
len()           : Returns length of object | len([1, 2, 3]) → 3
list()          : Creates a list | list('abc') → ['a', 'b', 'c']
locals()        : Returns dictionary of local symbol table | locals()

# M
map()           : Applies function to all items | map(str, [1, 2, 3]) → ['1', '2', '3']
max()           : Returns largest item | max([1, 5, 3]) → 5
memoryview()    : Returns memory view object | memoryview(bytes(5))
min()           : Returns smallest item | min([1, 5, 3]) → 1

# N
next()          : Gets next item from iterator | next(iter([1, 2]))

# O
object()        : Returns a new featureless object | object()
oct()           : Converts integer to octal string | oct(8) → '0o10'
open()          : Opens a file | open('file.txt', 'r')
ord()           : Returns Unicode code point of character | ord('A') → 65

# P
pow()           : Returns power of number | pow(2, 3) → 8, pow(2, 3, 5) → 3
print()         : Prints to console | print('Hello')
property()      : Returns property attribute | @property

# R
range()         : Returns sequence of numbers | range(5) → [0, 1, 2, 3, 4]
repr()          : Returns string representation | repr('hello') → "'hello'"
reversed()      : Returns reversed iterator | reversed([1, 2, 3]) → [3, 2, 1]
round()         : Rounds a number | round(3.7) → 4, round(3.14159, 2) → 3.14

# S
set()           : Creates a set | set([1, 2, 2, 3]) → {1, 2, 3}
setattr()       : Sets attribute value | setattr(obj, 'name', 'value')
slice()         : Returns slice object | slice(1, 5, 2)
sorted()        : Returns sorted list | sorted([3, 1, 2]) → [1, 2, 3]
staticmethod()  : Converts method to static method | @staticmethod
str()           : Converts to string | str(123) → '123'
sum()           : Sums items of iterable | sum([1, 2, 3]) → 6
super()         : Returns proxy object for parent class | super().__init__()

# T
tuple()         : Creates a tuple | tuple([1, 2, 3]) → (1, 2, 3)
type()          : Returns type of object | type(5) → <class 'int'>

# V
vars()          : Returns __dict__ of object | vars(obj)

# Z
zip()           : Aggregates elements from iterables | zip([1,2], ['a','b']) → [(1,'a'), (2,'b')]

# Special
__import__()    : Imports module programmatically | __import__('math')
"""


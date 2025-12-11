# 📃 How to work with Text, CSV and JSON Files

"""
Python File Modes Reference
============================

Open (file, mode):  Function that opens provided file as a file object in
                    the specified mode (read/ write/ append/ create)

Example:
    filename = 'example.txt'
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


File Mode Reference Table
-------------------------
                | r    r+   w    w+   a    a+
----------------+----------------------------------
read            | +    +         +         + 
write           |      +    +    +    +    +
write after seek|      +    +    +
create          |           +    +    +    +
truncate        |           +    +
position at start| +  +    +    +
position at end |                     +    +


Mode Meanings:
--------------
• r   - read mode (default): file must exist
• r+  - read and write: file must exist, can read and write
• w   - write mode: creates new file or truncates existing file
• w+  - write and read: creates file, truncates if exists
• a   - append mode: creates file if doesn't exist, writes at end
• a+  - append and read: creates file, reads anywhere, writes at end
• b   - binary mode (add to any mode, e.g., 'rb', 'wb')
• t   - text mode (default, can be explicit: 'rt', 'wt')

Definitions:
• read - reading from file is allowed
• write - writing to file is allowed
• create - file is created if it does not exist yet
• truncate - during opening of the file it is made empty (all content erased)
• position at start - after file is opened, initial position is at the start
• position at end - after file is opened, initial position is at the end
"""

import os


#1️⃣ Example 1: Read file with correct path
# file_2.txt is located in NewFolder/Folder_A/
filename = os.path.join('NewFolder', 'Folder_A', 'file_2.txt')

# # Check if file exists before opening
# if os.path.exists(filename):
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)
#     file.close()
# else:
#     print(f"Error: File '{filename}' not found!")


# 2️⃣  
#-------------------------------------------------------
with open(filename, 'r') as file:
    content = file.read()
    print(content) 

    for n, line in enumerate(content.splitlines()):
        print(n, line)
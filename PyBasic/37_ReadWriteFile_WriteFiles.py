# Write Files 
#-------------------------------------------------
filename = './NewFolder/Folder_Re_A/example_003.txt'

# # Example 1: this is a bad example because úsing 'w'can overwrite files instead use  Example2!
# with open(filename, 'w') as f:
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')
#     f.write('Hello!\n')


# Example 2
import os

filename = './NewFolder/Folder_Re_A/example_005.txt'

if not os.path.exists(filename):
    print(f"Creating a New File: {filename}")
    with open(filename, 'w') as files:
        files.write('Hello!\n')
        files.write('Hello!\n')
        files.write('Hello!\n')
        files.write('Hello!\n')
        files.write('Hello!\n')
else:
    print("File Exists!")

    print('Content: ')
    with open(filename, 'r') as files:
        print(files.read())


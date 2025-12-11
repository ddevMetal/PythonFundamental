import os

# r - raw string (prevents backslash from being treated as escape character)
path = r"C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic\NewFolder"

#1️⃣ Check if Folder Exists
if os.path.exists(path):
    print("Path Exits.")
else:
    print("Path Doesn't Exists.")
    # Create new Folder (os.makedirs creates all intermediate directories)
    os.makedirs(path)
    print(f'📁 Folder created Successfully!')



#2️⃣ Join Paths and Create Multiple Folders
# Define the base path where we want to create folders
path = r"C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic\NewFolder"

# List of folder names to create
list_folder = ['Folder_A', 'Folder_B', 'Folder_C']

# Loop through each folder name and create it
for folder in list_folder:
    # Join the base path with the folder name (cross-platform compatible)
    new_path = os.path.join(path, folder)

    # Check if folder exists before creating
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print('Created Folder: {}'.format(folder))


# # 3️⃣ Rename Items : Method 1
# # Specify the folder containing files to rename
# path = r"C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic\NewFolder\Folder_A"

# # Loop through all files in the directory
# for filename in os.listdir(path):
#     print(filename)

#     # Check if the target filename exists
#     if 'file_1.txt' in filename:
#         # Replace old name with new name
#         new_filename = filename.replace('file_1.txt', 'newFile1.txt')
#         # Rename the file (need full paths for both old and new names)
#         os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
#         print('Renamed File: {} to {}'.format(filename, new_filename))


# # 3️⃣ Rename Items : Method 2
# path = r"C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic\NewFolder\Folder_A"

# for filename in os.listdir(path):
#     print(f'Example 2 File Name: ---> {filename} \t:D')

#     # Check if the target file name exists
#     if 'newFile1.txt' in filename:
#         new_filename2 = filename.replace('newFile1.txt', 'newFile2.txt')

#         abs_old_filepath = os.path.join(path, filename)
#         abs_new_filepath = os.path.join(path, new_filename2)
#         os.rename(abs_old_filepath, abs_new_filepath)

#         print('Renamed File: {} to {}'.format(abs_old_filepath, abs_new_filepath))



#4️⃣ Get Nested Folder 
path = r"C:\Users\tchou\GitHub\pythonProj\PythonFundamental\PyBasic"

for root, dirs, files in os.walk(path):
    print(f'\nDirectory: {root}')

    for dir in dirs:
        print('Sub-Folder: ' + dir)

    for file in files:
        print('File: ' + file)
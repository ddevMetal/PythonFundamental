import os

#1️⃣ Read Text Files
#--------------------------------------------

# with the with statement, it will automatically close the file
# don't required to put file.close()

path = "./NewFolder/Folder_Re_A"
filename = os.path.join(path, "example_001.txt")  # ✅ Correct

with open(filename, 'r') as file:
    content = file.read()
    # print(content)

    for n, line in enumerate(content.splitlines()):
        print(f'{n+1}: {line}')
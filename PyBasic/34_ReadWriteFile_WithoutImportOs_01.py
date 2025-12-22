## Read, Write, and Append File 


# Basics
'''
Using the open(file, mode) function

Function that opens provided file as file object n the specified mode(read/ write/ append/ create).

'''


path = "./NewFolder/Folder_Re_A/"
filename = 'example_001.txt'
fullpath = path + filename
file = open(fullpath, 'r')
content = file.read()
print(content)
file.close()
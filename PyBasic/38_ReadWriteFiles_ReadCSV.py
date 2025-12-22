# CSV FILES
# -----------------------------------
import csv

# Read CSV Files
filename = './NewFolder/Folder_Re_A/items.txt'

with open(filename, 'r') as files:
    reader = csv.reader(files)
    for row in reader:
        print(row)
        for item in row:
            print(item)
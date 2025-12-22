# # Write CSV Files
# import csv
# from helper import getFullPath

# filename = getFullPath("","", 'items.txt')
# with open(filename, 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['sexy1' , 'sex' , '100'])

# Write CSV Files
import csv
from helper import getFullPath

filename = getFullPath("","", 'items.txt')
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['sexy1' , 'sex' , '100'])
    writer.writerow(['sexy1' , 'sex' , '100'])
    writer.writerow(['sexy1' , 'sex' , '100'])
    writer.writerow(['sexy1' , 'sex' , '100'])
    writer.writerow(['sexy1' , 'sex' , '100'])


# BECAREFUL WHEN USING 'a' and 'w' <-- append wont ovewrite existing file, write will.
import os
from datetime import datetime


# Append Text
#---------------------------------------------------------

path = "./NewFolder/Folder_Re_A"
filename = os.path.join(path, "example_002.txt")

# Get current date and time
now = datetime.now()
formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open(filename, 'a+') as f:
    f.write('Hello World' + " " + formatted_date_time + "\n")
    f.write('Hello World' + " " + formatted_date_time + "\n")
    f.write('Hello World' + " " + formatted_date_time + "\n")
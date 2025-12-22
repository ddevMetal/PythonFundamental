"""
Excel on Python 

documentation: 
https://openpyxl.readthedocs.io/en/stable/
https://ssopenpyxl.readthedocs.io/en/stable/#introduction
"""
from openpyxl import *
import os

filename = "./NewFolder/Excel/Example.xlsx"

# 📝 Create a new Excel file if it doesn't exist or is invalid
#---------------------------------------------------

wb      = load_workbook(filename)

# get Worksheets from workbook
# ws = wb.active            # Get active Worksheet
ws = wb['Materials']        # Get Sheet by name
all_ws = wb.worksheets
all_ws_names = wb.sheetnames

for ws in all_ws:
    print(ws.title)

# print(ws)
# print(all_ws)
# print(all_ws_names)


# Create/Copy/Remove Worksheets
# -------------------------------------------
new_ws = wb.copy_worksheet(ws)
new_ws.title = 'Copy!'

wb.save(filename) # Override the files!


# Create new Worksheet
#-----------------------------------------
new_ws = wb.create_sheet('NewSheet1')
wb.save(filename)

# Remove sheet
ws_to_remove = wb['NewSheet1']
wb.remove(ws_to_remove)     # remove worksheet
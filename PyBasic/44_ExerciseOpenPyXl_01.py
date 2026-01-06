import os
from openpyxl import Workbook

# Example
data = [
    ['Room Number', 'Room Name' ,'Area (sqm)' ,'Occupancy', 'Finishes'         ],
    ['101'        , 'Lobby'     , 35          , 50         , 'Marble Floor'    ],
    ['102'        , 'Conference', 50          , 100        , 'Carpeted Floor'  ],
    ['103'        , 'Office'    , 20          , 5          , 'Wooden Floor'    ]
]

# Create a new workbook + worksheet
wb = Workbook()
ws = wb.active
ws.title = 'EF - Rooms'


# Seperate data into rows and columns
headings = data[0]
data     = data[1:]


# Write headings to worksheet
from openpyxl.styles import Font
for col_num, heading in enumerate(headings, start=1):
    cell = ws.cell(row=1, column=col_num, value=heading)
    cell.font = Font(bold=True, sze=16)
    
# Write data to worksheet
for row in data:
    ws.append(row)
    
# Save workbook to file
filename = 'EF-Rooms.xlsx'
wb.save(filename)

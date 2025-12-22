from helper import getFullPath
import json

#2️⃣ Append to JSON
#----------------------------------------------------

filename = getFullPath("", "", 'materials.json')

# Read JSON
with open(filename, 'r') as f:
    data  = json.load(f)


# New materials 
new_materials = {   "id"                 : "M005",
                    "name"               : "Plaster",
                    "density"            : 123421,
                    "cost_per_1000_unit" : 100
                }

# Append new material
data['materials'].append(new_materials)

# Overide the file
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# HANDLING JSON FILE
import json
from helper import getFullPath

#1️⃣ Read JSON Files
#------------------------------------------------
filename = getFullPath("","",'materials.json')
with open(filename, 'r') as f:
    
    data = json.load(f)
    
    # Print entire data structure
    print("Full data:")
    print(data)
    print(f"\nType: {type(data)}\n")
    
    # Access materials array
    mats = data['materials']
    
    # Print each material
    print("Materials:")
    for mat in mats:
        print(mat)
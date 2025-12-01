from helper import br, ctitle

# List Operators
#------------------------------------------------------------
mats_1 = ["Concrete", "Steel", "Glass"]
mats_2 = ["Wood", "Brick"]
mats_3 = mats_1 + mats_2
list_materials = mats_1
mats_4 = [mats_1, mats_2]


print(mats_3)
br(50)

# # Multiple List
# #------------------------------------------------------------
# print(mats_1*10)
# br(50)

# Membership Operators
#------------------------------------------------------------
print('Concrete'     in list_materials)     #True
print('Wool'         in list_materials)     #False
print('Wool'         not in list_materials) #True
br(50)

# Equality
#------------------------------------------------------------
print(mats_1 == mats_2)                     #False
print(mats_1 != mats_2)                     #True
br(50)

print(mats_2 in mats_3) # False unless list inside a list / join list !=
print(mats_2 in mats_4) # True list inside a list [ ["Concrete", "Steel", "Glass"], ["Wood", "Brick"]   ]

# Equality
#------------------------------------------------------------
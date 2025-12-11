# import sys

# print('before')
# if 50<10:
#     sys.exit()
# print('after')

#-----------------------------------------------------------

# DATE TIME
"""
rom datetime import datetime

now = datetime.now()

# Common formats
print(now.strftime("%Y-%m-%d"))           # 2025-12-12
print(now.strftime("%d/%m/%Y"))           # 12/12/2025
print(now.strftime("%B %d, %Y"))          # December 12, 2025
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2025-12-12 14:30:45
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%A, %B %d, %Y"))      # Thursday, December 12, 2025

"""
from datetime import datetime

now                 = datetime.now()
formatted_date      = now.strftime("%Y-%m-%d")
formatted_time      = now.strftime("%H:%M:%S")
formatted_date_time = now.strftime("%Y=%m-%d %H:%M:%S")


print(formatted_date)
print(formatted_time)
print(formatted_date_time)


#-----------------------------------------------------------

# TIME MODULE
import time

for i in range (1):
    time.sleep(1)
    print('{second has pass')









#-----------------------------------------------------------

# MATH 
import math

num = 14
root = math.sqrt(num)
print(root)

# Pi
r = 3
area = math.pi * r**2
print(area)

#Ceiling (Round UP)/ Floor (Round Down)
num = 15.7
ceil_num    = math.ceil(num)
floor_num   =  math.floor(num)
print(ceil_num, '<-- Ceiling')
print(floor_num, '<-- Floor')

#RANDOM
import random

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)

print(R, G, B)


# Radom Item Selector
materials           = ['Wood', 'Glass', 'Brick', 'Concrete']
random_materials    = random .choice(materials)
print(random_materials)
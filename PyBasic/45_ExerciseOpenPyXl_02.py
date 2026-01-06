import pandas as pd
from openpyxl import Workbook
import numpy as np


# Data for biggest building 

data = {
    "Project Name" : [
        "Burj Khalifa",
        "Shanghai Tower",
        "Abraj Al-Bait Clock Tower",
        "Ping An Finance Center",
        "Lotte World Tower"
    ],
    "Height (m)" : [
        828,
        632,
        601,
        599,
        555
    ],
    "Country" : [
        "UAE",
        "China",
        "Saudi Arabia",
        "China",
        "South Korea"
    ],
    "City" : [
        "Dubai",
        "Shanghai",
        "Mecca",
        "Shenzhen",
        "Seoul"
    ],
    "Floors" : [
        163,
        128,
        120,
        115,
        123
    ]
}

# create 
df = pd.DataFrame(data)

# print(df)

df.to_excel("biggest_buildings.xlsx", index=False)
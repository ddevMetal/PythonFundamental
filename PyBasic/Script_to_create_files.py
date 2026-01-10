import os
import random
import json
import csv
from openpyxl import Workbook

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
BASE_PATH = "/home/cm/Documents/GitHub/PythonFundamental/PyBasic/Generated_Files"
os.makedirs(BASE_PATH, exist_ok=True)

WORDS = [
    "lorem", "ipsum", "data", "python", "inventory",
    "system", "random", "file", "business", "account",
    "invoice", "quotation", "customer", "product"
]

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def random_sentence():
    return " ".join(random.choices(WORDS, k=random.randint(8, 15))).capitalize() + "."

def random_paragraph():
    return "\n".join(random_sentence() for _ in range(random.randint(4, 7)))

def random_inventory_item():
    return {
        "item_id": random.randint(1000, 9999),
        "name": random.choice(["Keyboard", "Mouse", "Monitor", "Laptop", "Printer"]),
        "quantity": random.randint(1, 100),
        "price": round(random.uniform(10, 1500), 2)
    }

# --------------------------------------------------
# TXT FILES
# --------------------------------------------------
for i in range(1, 11):
    with open(f"{BASE_PATH}/text_{i}.txt", "w") as f:
        paragraphs = random.randint(10, 100)
        for _ in range(paragraphs):
            f.write(random_paragraph() + "\n\n")

# --------------------------------------------------
# CSV FILES
# --------------------------------------------------
for i in range(1, 40):
    with open(f"{BASE_PATH}/inventory_{i}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["item_id", "name", "quantity", "price"])
        for _ in range(20):
            item = random_inventory_item()
            writer.writerow(item.values())

# --------------------------------------------------
# JSON FILES
# --------------------------------------------------
for i in range(1, 47):
    data = [random_inventory_item() for _ in range(20)]
    with open(f"{BASE_PATH}/inventory_{i}.json", "w") as f:
        json.dump(data, f, indent=4)

# --------------------------------------------------
# XLSX FILES
# --------------------------------------------------
for i in range(1, 132):
    wb = Workbook()
    ws = wb.active

    file_type = random.choice(["Invoice", "Quotation", "Account"])
    ws.append([file_type])
    ws.append(["ID", "Description", "Amount"])

    for _ in range(10):
        ws.append([
            random.randint(1000, 9999),
            random.choice(["Service Fee", "Product Sale", "Maintenance"]),
            round(random.uniform(50, 5000), 2)
        ])

    wb.save(f"{BASE_PATH}/{file_type.lower()}_{i}.xlsx")

print("✅ Random files generated successfully!")

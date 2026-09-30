import csv

with open("data/data.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

with open("prepared.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("Data prepared successfully")
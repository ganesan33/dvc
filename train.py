import csv

with open("prepared.csv", "r") as f:
    reader = csv.DictReader(f)

    total = 0
    count = 0

    for row in reader:
        marks = float(row["marks"])
        total += marks
        count += 1

if count == 0:
    print("Error: No data found in prepared.csv")
    exit()

average = total / count

with open("model.txt", "w") as f:
    f.write(str(average))

print("Training completed")
print("Average marks:", average)
import csv
import json

with open("model.txt", "r") as f:
    average = float(f.read())

with open("prepared.csv", "r") as f:
    reader = csv.DictReader(f)

    errors = []

    for row in reader:
        actual = float(row["marks"])

        error = abs(actual - average)

        errors.append(error)

mean_error = sum(errors) / len(errors)

metrics = {
    "mean_error": mean_error
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print("Evaluation completed")
print("Mean error:", mean_error)
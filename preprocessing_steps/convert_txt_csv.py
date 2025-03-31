import csv

# File paths
input_file = "data.txt"     # Change to your file name
output_file = "data.csv"

# Column headers based on the dataset description
headers = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]

with open(input_file, "r") as txt_file, open(output_file, "w", newline='') as csv_file:
    reader = csv.reader(txt_file)
    writer = csv.writer(csv_file)

    # Write the headers first
    writer.writerow(headers)

    # Then write all the data rows
    for row in reader:
        writer.writerow(row)

print("CSV file created successfully with headers.")

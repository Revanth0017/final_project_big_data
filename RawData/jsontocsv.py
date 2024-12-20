import json
import csv

# Load JSON data
with open('exchange_data.json', 'r') as json_file:
    data = json.load(json_file)

# Define the CSV file name
csv_file_name = 'exchange_data.csv'

# Collect all possible headers (keys) from all records
headers = set()
for row in data:
    headers.update(row.keys())

# Open CSV file for writing
with open(csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    writer = csv.DictWriter(csv_file, fieldnames=sorted(headers))

    # Write headers (fieldnames are already sorted for consistent order)
    writer.writeheader()

    # Write the rows of data
    for row in data:
        # Fill missing keys with None or an empty string for each row
        writer.writerow({key: row.get(key, '') for key in headers})

print(f"Data has been successfully converted to {csv_file_name}")

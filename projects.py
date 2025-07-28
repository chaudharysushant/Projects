import csv

file_path = r'C:\Users\Sushant-Chaudhary\Desktop\Projects\people_output.csv'

# Data to write (a list of dictionaries)
data = [
    {'name': 'Sushant Chaudhary', 'email': 'sushant.chaudhary@example.com', 'isActive': True},
    {'name': 'John Doe', 'email': 'john.doe@example.com', 'isActive': False}
]

with open(file_path, 'w', newline='') as file:
    fieldnames = ['name', 'email', 'isActive']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write rows
    for row in data:
        writer.writerow(row)

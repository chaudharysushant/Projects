import csv

file_path = r'C:\Users\Sushant-Chaudhary\Desktop\Projects\people.csv'

with open(file_path, 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

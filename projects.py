import csv

FILE_PATH = r'C:\Users\Sushant-Chaudhary\Desktop\Projects\contacts.csv'

def view_contacts():
with open(FILE_PATH, 'r') as file:
    reader = csv.DictReader(file)
    for contacts in reader:
        print(f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}")
